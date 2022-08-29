frameworks=[
    {"fwname":"django","language":"python","rating":5},#fw
    {"fwname": "flask", "language": "python", "rating": 3},
    {"fwname": "angular", "language": "typescript", "rating": 5},
    {"fwname": "react", "language": "javascript", "rating": 4},
    {"fwname": "spring", "language": "java", "rating": 4},
    {"fwname": "ASP", "language": "c#", "rating": 5},

]


# framework_names = [fw.get('fwname') for fw in frameworks]
# print(framework_names)


# language_names = [fw.get('language') for fw in frameworks]
# print(language_names)


# most_rated = [fw.get('fwname') for fw in frameworks if fw.get('rating') > 4]
# print(most_rated)


# py_fw = [fw.get('fwname') for fw in frameworks if fw.get('language') == 'python']
# print(py_fw)


# top_rated = max(frameworks, key=lambda fw: fw.get('rating'))
# print(top_rated)


# low_rated = min(frameworks, key=lambda fw: fw.get('rating'))
# print(low_rated)

# frameworks.sort(key=lambda fw: fw.get('rating'))
# print(frameworks)

frameworks.sort(key=lambda fw: fw.get('rating'), reverse=True)
print(frameworks)
