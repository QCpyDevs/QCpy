# import numpy as np
# from qcpy import quantumcircuit

# def inc(x):
#     qc = quantumcircuit(qubits=x, prep="z", gpu = True)
#     qc.h(0)
#     qc.h(1)
#     qc.h(2)
#     qc.h(3)
#     qc.h(4)
#     qc.h(5)
#     qc.rxx(0, 1)
#     qc.rxx(2, 3)
#     qc.rxx(4, 5)
#     qc.rx(5)
#     return np.around(qc.state.flatten(), 3)

# def test_16a():
#     assert (
#         inc(6)
#         == np.array(
#             [
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#                 -0.125 + 0j,
#             ],
#             'F',
#         )
#     ).all(), "test_16a Failed on hadamard (x6) -> rxx (x3) -> rx"
