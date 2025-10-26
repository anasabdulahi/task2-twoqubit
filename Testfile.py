
import numpy as np
from TaskTwo import prepare_state, prepare_state_n
#checking its normalised
def test_normalises_two_qubit_state():
    v = prepare_state([2, 1, 0, 1j])
    assert np.isclose(np.linalg.norm(v), 1.0), "State is not normalised to 1."
#checks they're not all 0
def test_rejects_zero_vector():
    import pytest
    with pytest.raises(ValueError):
        prepare_state([0, 0, 0, 0])
#checks length 
def test_rejects_wrong_length():
    import pytest
    with pytest.raises(ValueError):
        prepare_state([1, 0, 0])  # only 3 amplitudes, should fail
#checks three quibit works
def test_generalises_to_three_qubits():
    v = prepare_state_n([1, 0, 0, 0, 0, 0, 0, 0])
    assert np.isclose(np.linalg.norm(v), 1.0), "3-qubit state not normalised."
print("stfu pussy")