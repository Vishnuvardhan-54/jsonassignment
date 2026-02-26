import numpy as np
#TASK1
np.random.seed(42)

scores=np.random.randint(50,100,size=(5,4))

print("scores array:\n",scores)

print("\n3rd student in the 2nd subject: ",scores[2,1])

print("\nlast 2 students(all sub):\n",scores[-2:,:])

print("\nfirst 3 students in subjects 2 & 3 :\n",scores[:3,1:3])

print("-"*60)

#TASK2

col_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise mean:", col_mean)

curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

curved_scores = np.clip(curved_scores, None, 100)

print("\nCurved scores:\n", curved_scores)

# Row wise max (best subject per student)
row_max = curved_scores.max(axis=1)
print("\nRow-wise max per student:", row_max)

print("-"*60)



#TASK3

# Min-max normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)
print("\nNormalized scores:\n", normalized)

# Index of single highest value in normalized array
flat_index = np.argmax(normalized)
student_idx, subject_idx = np.unravel_index(flat_index, normalized.shape)

print("\nHighest normalized value at:")
print("Student index:", student_idx)
print("Subject index:", subject_idx)

# All scores strictly above 90 from curved_scores
above_90 = curved_scores[curved_scores > 90]
print("\nScores above 90:", above_90)