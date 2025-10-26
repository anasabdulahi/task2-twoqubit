import numpy as np  

def prepare_state(amplitudes):
   
    if len(amplitudes) != 4:
        raise ValueError("A two-qubit state needs 4 amplitudes.")
    
    state = np.array(amplitudes, dtype=complex)

    if np.all(state == 0):
        raise ValueError("All amplitudes are zero so can't normalise")

    norm = np.sqrt(np.sum(np.abs(state)**2))

    state = state / norm

    basis = ["|00>", "|01>", "|10>", "|11>"]
    print("Normalised state vector:")
    for label, amp in zip(basis, state):
        print(f"  {label}: {amp}")

    probabilities = np.abs(state)**2
    print("\nProbabilities for each basis state:")
    for label, p in zip(basis, probabilities):
        print(f"  P({label}) = {p:.3f}")

    return state


#General version for n qubits
def prepare_state_n(amplitudes):
  
    state = np.array(amplitudes, dtype=complex)
    m = len(state)

    if m & (m - 1):
        raise ValueError("Number of amplitudes must be a power of two.")

    if np.all(state == 0):
        raise ValueError("All amplitudes are zero so can't normalise")

    state = state / np.sqrt(np.sum(np.abs(state)**2))
    return state

#so it doesnt run every time
if __name__ == "__main__":
    amplitudes = [0, 1, 0, 0]
    state = prepare_state(amplitudes)
