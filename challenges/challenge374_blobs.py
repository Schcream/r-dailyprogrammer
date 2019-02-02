#https://www.reddit.com/r/dailyprogrammer/comments/aldexk/20190130_challenge_374_intermediate_the_game_of/ [INTERMEDIATE]
import numpy as np

def chebyshev_distance(b1,b2):
	return max([np.abs(b1[i]-b2[i]) for i in range(len(b1)-1)])

#Blobs
blobs = np.array([[0,3,2,1],[2,1,1,2],[1,15,2,4]])
print(blobs)
input()
while np.sum(((blobs[:,-1] - blobs[0,-1]) == 0)) - np.size(blobs,0) < 0:

	new_blobs = np.array([[-1]*np.size(blobs[0])])
	for b in blobs:
		
		#get dist to other and smaller blobs
		dist = np.array([[b,1000]])
		for b_ in blobs:
			if not np.array_equal(b, b_) and b_[-1]<b[-1]:
				dist = np.append(dist, [[b_,chebyshev_distance(b,b_)]], axis=0)

		#print("dist", dist)
		if np.size(dist,0) > 1:
			#print("here")
			closest = dist[np.argmin(dist[1:,1])+1][0]
			move = np.array([])
			for x in closest[:-1] - b[:-1]:
				move = np.append(move, min(1, max(-1, x)))
		else:
			move = [0]*(np.size(blobs[0])-1)

		new_b = np.append(b[:-1] + move, b[-1])
		duplicate = False
		for b_ in new_blobs:
			#print(new_blobs, new_b)
			if np.array_equal(new_b[:-1], b_[:-1]):
				b_[-1] += new_b[-1]
				duplicate = True

		if not duplicate:
			new_blobs = np.append(new_blobs, [new_b], axis=0)

	blobs = new_blobs[1:]
	print(blobs)
	input()

print(blobs)
