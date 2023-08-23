# 1. 클래스 생성
class Member():
    # 2. Member 클래스 속성
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # 3. Member 클래스 메소드
    def display(self):
        print(f'이름: {self.name}, 아이디: {self.username}')


class Post():
    # 4. Post 클래스 속성
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


members = []
posts = []

# 5. 회원 인스턴트 생성 및 저장
m1 = Member('솔','sol','sol727')
m2 = Member('오레오','oreo','oreo0124')
m3 = Member('쿨피스','piece','password')

members.append(m1)
members.append(m2)
members.append(m3)

# 5-a. 회원 이름 출력
for member in members:
    print(member.name)

    # 6. 회원당 개시글 3개 작성 후 인스턴스 저장
    p1 = Post(f'내 이름은 {member.name}', '백수죠.', member.name)
    p2 = Post('지금 시간은', '아무튼 새벽임', member.name)
    p3 = Post('내 아이디는', member.username, member.name)
    posts.append(p1)
    posts.append(p2)
    posts.append(p3)

# 6-a. 특정 유저의 게시글 전부 제목 프린트
for post in posts:
    if post.author == '오레오':
        print(post.title)

# 6-b. contents에 특정 단어가 포함된 게시글 전부 제목 프린트
for post in posts:
    dead = post.content.find('백수')
    if dead != -1:
        print(post.title)


# 추가 도전 과제 - 1
make_member = input('회원정보를 생성하시겠습니까? Yes/No ')

if make_member in ['Yes','yes','YES']:
    name = input('이름: ')
    username = input('아이디: ')
    password = input('비밀번호: ')

    member = Member(name, username, password)
    members.append(member)

# 추가 도전 과제 - 2
while True:

    print('게시글 작성하기')

    title = input('제목: ')
    content = input('내용: ')
    author = member.username

    post = Post(title, content, author)
    posts.append(post)
    print('작성한 내용 확인')
    print(f'제목: {post.title}')
    print(f'작성자: {post.author}')
    print(f'내용: {post.content}')

    check = input('게시글을 더 작성하시겠습니까? yes/no ')
    if check in ['Yes', 'yes', 'YES']:
        continue
    else:
        break
