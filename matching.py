from gensim.models import Word2Vec
import random

# ダミーデータの生成
common_hobbies = ["hobby1", "hobby2", "hobby3", "hobby4", "hobby5"]
users = []
for i in range(10):
    hobbies = random.sample(common_hobbies, 3) + [f"hobby{i}{j}" for j in range(2)]
    users.append((f"user{i}", hobbies))

# Word2Vecモデルの学習
hobbies = [hobby for _, hobbies in users for hobby in hobbies]
random.shuffle(hobbies)
model = Word2Vec(sentences=[hobbies], min_count=1, window=5, epochs=10, vector_size=100)

# マッチングの実行
matches = []
for i, user1 in enumerate(users):
    for j, user2 in enumerate(users[i + 1 :], i + 1):
        shared_hobbies = set(user1[1]) & set(user2[1])
        if shared_hobbies:
            score = sum(
                [model.wv[hobby][k] for hobby in shared_hobbies for k in range(10)]
            ) / len(shared_hobbies)
            matches.append((user1[0], user2[0], score))

# スコアが高い順にソートして出力
for match in sorted(matches, key=lambda x: x[2], reverse=True):
    print(f"{match[0]} and {match[1]} matched with a score of {match[2]}")
if not matches:
    print("No matches found")
