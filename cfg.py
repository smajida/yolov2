import numpy as np

N_CLASSES     = 31
ANCHORS       = np.array(((0.023717899133663362, 0.035715759075907606),
(0.059577141608391594, 0.08738709207459215),
(0.08816276658767774, 0.1294924960505529),
(0.03283318210930825, 0.0483890193566751),
(0.04450034340659346, 0.064308608058608)))

# HYPER-PARAMETERS
BATCH_SIZE = 8
EPOCHS     = 10
LEARN_RATE = 1e-5
