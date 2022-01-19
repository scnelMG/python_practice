# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file)) #close 필요없음

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("오킹의 방송은 재밌다")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


