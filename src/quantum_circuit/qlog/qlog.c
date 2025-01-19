#include "qlog.h"
#define MAX_QLOG_LENGTH (10000)
#define EMPTY_QLOG (MAX_QLOG_LENGTH + 1000)
#define MAX_STR_LENGTH (30)
#define MAX_QLOG_QUBITS (256)
#define MATRIX_UNITARY_FORMAT (2)
#define IS_QLOG_EMPTY(qlog) (qlog->qlog_size == EMPTY_QLOG)
#define GATE_TYPE_TO_STRING (qlog_entry_gate) (gate_names[qlog_entry_gate])


struct qlog_def* qlog_init(uint8_t qubits) {
  struct qlog_def* qlog = (struct qlog_def*)malloc(sizeof(struct qlog_def));
  if (qlog == NULL) {
    return NULL;
  }
  qlog->qlog_qubit_cnt = qubits;
  qlog->qlog_size = 0;
  qlog->qlog_entries = (qlog_entry_def**)malloc(MAX_QLOG_LENGTH * sizeof(qlog_entry_def*));
  if (qlog->qlog_entries == NULL) {
    free(qlog);
    return NULL;
  }
  struct qlog_stats_def qlog_stat = {0};
  qlog->qlog_stat = qlog_stat;
  return qlog;
}

void qlog_delete(struct qlog_def* qlog) {
  for (uint16_t i = 0; i < qlog->qlog_size; ++i) {
    qlog_entry_delete(qlog->qlog_entries[i]);
  }
  free(qlog->qlog_entries);
  qlog->qlog_entries = NULL;
  free(qlog);
  qlog = NULL;
  return; 
}

uint16_t qlog_size(struct qlog_def *qlog) {
  return !qlog ? (uint16_t)EMPTY_QLOG : qlog->qlog_size;
}

void qlog_clear(struct qlog_def *qlog) {
  if (!qlog) {
    return;
  }
  for (uint16_t i = 0; i < qlog->qlog_size; ++i) {
    qlog_entry_delete(qlog->qlog_entries[i]);
  }
  qlog->qlog_size = EMPTY_QLOG;
  return;
}

qlog_append_res qlog_append(struct qlog_def *qlog, uint8_t *qubits, uint8_t num_qubits, int type, int gate) {
  if (!qlog) {
    return QLOG_APPEND_ERROR;
  }
  if (qlog->qlog_size > MAX_QLOG_LENGTH) {
    return QLOG_APPEND_FULL; 
  }
  if (qlog->qlog_size == EMPTY_QLOG) {
    qlog->qlog_size = 0;
  }
  qlog->qlog_entries[qlog->qlog_size] = qlog_entry_init(qubits, num_qubits, type, gate, qlog->qlog_size);
  if (!qlog->qlog_entries[qlog->qlog_size]) {
    return QLOG_APPEND_ERROR;
  }
  qlog->qlog_size += 1;
  return QLOG_APPEND_SUCCESS;
}

void qlog_dump_content(struct qlog_def *qlog, bool verbose) {
  if (!qlog) {
    return;
  }
  if (IS_QLOG_EMPTY(qlog)) {
    printf("qlog is empty\n.");
  }
  if (verbose) {
    printf("qlog size: %d, number of qubits: %d\n", qlog->qlog_size, qlog->qlog_qubit_cnt);
    // get stats from qlog in small table
  } 
  for (uint16_t i = 0; i < qlog->qlog_size; i++) {
    printf("Entry: %d\n", i + 1);
    qlog_entry_dump_content(qlog->qlog_entries[i], verbose);
    printf("\n");
  }
  return;
}

char** qlog_get_gate_names(struct qlog_def *qlog) {
  if (!qlog) {
    return NULL;
  }
  char** gate_names = (char**)malloc(sizeof(char*) * qlog->qlog_size * MAX_STR_LENGTH);
  for (uint16_t i = 0; i < qlog->qlog_size; ++i) {
    gate_names[i] = (char*)get_qlog_entry_gate(qlog->qlog_entries[i]);
    printf("NAME: %s\n", gate_names[i]);
  }
  return gate_names;
}

char** qlog_get_gate_types(struct qlog_def* qlog) {
  if (!qlog) {
    return NULL;
  }
  char** gate_types = (char**)malloc(sizeof(char*) * qlog->qlog_size * MAX_STR_LENGTH);
  for (uint16_t i = 0; i < qlog->qlog_size; ++i) {
    gate_types[i] = (char*)get_qlog_entry_gate_type(qlog->qlog_entries[i]);
    printf("TYPE: %s\n", gate_types[i]);
  }
  return gate_types;
}

struct qlog_entry_def* qlog_entry_init(uint8_t *qubits, uint8_t num_qubits, int type, int gate, uint8_t qlog_qubits) {
  struct qlog_entry_def* qlog_entry = (struct qlog_entry_def*)malloc(sizeof(struct qlog_entry_def));
  if (!qlog_entry) {
    return NULL;
  }
  qlog_entry->qlog_entry_qubits = (uint8_t*)malloc(num_qubits * sizeof(uint8_t));
  if (!qlog_entry->qlog_entry_qubits) {
    return NULL;
  }
  memcpy(qlog_entry->qlog_entry_qubits, qubits, num_qubits);
  qlog_entry->qlog_entry_qubit_cnt = num_qubits;
  qlog_entry->qlog_entry_gate = gate;
  qlog_entry->qlog_entry_gate_type = type;
  qlog_entry->qlog_quantum_gate = quantum_gate_get_gate(gate, 0, 0, 0);
  return qlog_entry;
}

void qlog_entry_delete(struct qlog_entry_def *qlog_entry) {
  free(qlog_entry->qlog_entry_qubits); 
  qlog_entry->qlog_entry_qubits = NULL;
  free(qlog_entry);
  qlog_entry = NULL;
  return;
}

global_gate_name qlog_entry_qg_name(struct qlog_entry_def *qlog_entry) {
  return qlog_entry->qlog_entry_gate;
}

global_gate_type qlog_entry_qg_type(struct qlog_entry_def *qlog_entry) {
  return qlog_entry->qlog_entry_gate_type;
}

void qlog_entry_dump_content(struct qlog_entry_def *qlog_entry, bool verbose) {
  if (!qlog_entry) {
    return;
  }
  printf("(");
  if (verbose) {
    printf("Qubit Count: %d", qlog_entry->qlog_entry_qubit_cnt);
  }
  printf(" on: [");
  for (uint8_t i = 0; i < qlog_entry->qlog_entry_qubit_cnt; ++i) {
    printf("%d", qlog_entry->qlog_entry_qubits[i]);
    if (i + 1 != qlog_entry->qlog_entry_qubit_cnt) {
      printf(",");
    }
  }
  printf("] ");
  printf("%s, %s", get_qlog_entry_gate(qlog_entry), get_qlog_entry_gate_type(qlog_entry));
  printf(")");
  return;
}

const char* get_qlog_entry_gate(struct qlog_entry_def *qlog_entry) {
  return global_get_gate_name(qlog_entry->qlog_entry_gate);
}

const char* get_qlog_entry_gate_type(struct qlog_entry_def *qlog_entry) {
  return global_get_gate_type(qlog_entry->qlog_entry_gate_type);
}
