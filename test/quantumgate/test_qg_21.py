import numpy as np
from qcpy import gates


def test_qg_21():
    assert (
        gates.rzz()
        == np.array(
            [
                [np.exp(0 - 1j * ((np.pi / 2) / 2)), 0 + 0j, 0 + 0j, 0 + 0j],
                [0 + 0j, np.exp(0 + 1j * ((np.pi / 2) / 2)), 0 + 0j, 0 + 0j],
                [0 + 0j, 0 + 0j, np.exp(0 + 1j * ((np.pi / 2) / 2)), 0 + 0j],
                [0 + 0j, 0 + 0j, 0 + 0j, np.exp(0 - 1j * ((np.pi / 2) / 2))],
            ],
            "F",
        )
    ).all(), "test_qg_21 Failed on Rzz"
