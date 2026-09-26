# A1 passages (p0001-p0020). Question tuples:
#   ("mc", q, en, [correct, d1, d2, d3], [words], sentence)   correct option first; the
#                                                           generator rotates it into place
#   ("tf", q, en, True/False, [words], sentence)
P = []

P.append(dict(title="يوم أحمد", names=["أحمد", "القاهرة"], s=[
    ("اسمي أحمد، وأنا طالب في الجامعة.", "My name is Ahmad, and I am a university student."),
    ("أسكن مع أسرتي في بيت صغير في مدينة القاهرة.", "I live with my family in a small house in the city of Cairo."),
    ("في الصباح أشرب الشاي وآكل الخبز والجبن.", "In the morning I drink tea and eat bread and cheese."),
    ("بعد ذلك أذهب إلى الجامعة بالحافلة، لأن أبي يأخذ السيارة إلى عمله.",
     "After that I go to the university by bus, because my father takes the car to his work."),
    ("أدرس هناك حتى الساعة الثانية.", "I study there until two o'clock."),
    ("بعد الدرس آكل الغداء مع أصدقائي في مطعم قريب.", "After class I eat lunch with my friends in a nearby restaurant."),
    ("في المساء أساعد أمي في المطبخ.", "In the evening I help my mother in the kitchen."),
    ("ثم أقرأ كتابا أو أشاهد فيلما قبل أن أنام.", "Then I read a book or watch a film before I sleep."),
], q=[
    ("mc", "كيف يذهب أحمد إلى الجامعة؟", "How does Ahmad get to the university?",
     ["في الحافلة", "في سيارة أبيه", "في القطار", "مع أمه"], ["حافلة"], 3),
    ("tf", "يسكن أحمد في بيت كبير.", "Ahmad lives in a big house.", False, ["بيت", "صغير"], 1),
    ("tf", "يأكل أحمد الغداء مع أصدقائه.", "Ahmad eats lunch with his friends.", True, ["غداء", "صديق"], 5),
    ("mc", "ماذا يفعل أحمد في المساء؟", "What does Ahmad do in the evening?",
     ["يساعد أمه", "يعمل في مطعم", "يدرس في الجامعة", "يشرب القهوة"], ["مساء", "ساعد"], 6),
    ("tf", "يشرب أحمد القهوة في الصباح.", "Ahmad drinks coffee in the morning.", False, ["شرب", "صباح"], 2),
]))

P.append(dict(title="عائلة مريم", names=["مريم"], s=[
    ("هذه صورة عائلتي.", "This is a picture of my family."),
    ("أنا مريم، وعمري عشر سنوات.", "I am Maryam, and I am ten years old."),
    ("أبي طبيب في مستشفى كبير، وأمي معلمة في مدرسة.",
     "My father is a doctor in a big hospital, and my mother is a teacher in a school."),
    ("لي أخ واحد وأخت واحدة.", "I have one brother and one sister."),
    ("أخي كبير، وهو طالب في الجامعة.", "My brother is older, and he is a university student."),
    ("أختي صغيرة، وعمرها ثلاث سنوات فقط.", "My sister is little; she is only three years old."),
    ("جدي وجدتي يسكنان معنا في البيت.", "My grandfather and grandmother live with us in the house."),
    ("في يوم الجمعة نأكل الغداء في الحديقة.", "On Friday we eat lunch in the garden."),
    ("أحب عائلتي كثيرا.", "I love my family very much."),
    ("في المساء نجلس في الحديقة ونشرب الشاي.", "In the evening we sit in the garden and drink tea."),
    ("جدتي تقول لنا قصة جميلة كل ليلة، ثم ننام.", "My grandmother tells us a lovely story every night, then we sleep."),
], q=[
    ("mc", "ماذا يعمل أبو مريم؟", "What does Maryam's father do?",
     ["يعمل طبيبا", "يعمل معلما", "يعمل في مطعم", "يعمل في شركة"], ["طبيب", "مستشفى"], 2),
    ("tf", "لمريم أختان.", "Maryam has two sisters.", False, ["أخت", "واحد"], 3),
    ("tf", "الجد والجدة يسكنان في بيت آخر.", "The grandparents live in another house.", False, ["سكن", "بيت"], 6),
    ("mc", "أين تأكل العائلة الغداء يوم الجمعة؟", "Where does the family eat lunch on Friday?",
     ["في الحديقة", "في مطعم", "في المطبخ", "في المدرسة"], ["غداء", "حديقة"], 7),
    ("tf", "أخت مريم عمرها ثلاث سنوات.", "Maryam's sister is three years old.", True, ["أخت", "عمر"], 5),
]))

P.append(dict(title="في السوق", names=["خالد"], s=[
    ("يذهب خالد مع أمه إلى السوق يوم السبت.", "Khalid goes to the market with his mother on Saturday."),
    ("السوق كبير وفيه ناس كثيرون.", "The market is big and there are many people in it."),
    ("تشتري الأم الخبز والجبن والتفاح.", "The mother buys bread, cheese and apples."),
    ("يحب خالد الفاكهة، فيطلب من أمه تفاحا أحمر.", "Khalid loves fruit, so he asks his mother for red apples."),
    ("التفاح اليوم رخيص، لكن الجبن غال.", "Apples are cheap today, but the cheese is expensive."),
    ("بعد ذلك يشربان الشاي في مطعم صغير.", "After that the two of them drink tea in a small restaurant."),
    ("ثم يعودان إلى البيت بالحافلة، لأن معهما حقائب كثيرة.",
     "Then they go back home by bus, because they have a lot of bags with them."),
    ("في البيت تعمل الأم الغداء، ويساعدها خالد في المطبخ.", "At home the mother makes lunch, and Khalid helps her in the kitchen."),
    ("يقول خالد: هذا أفضل يوم في الأسبوع!", "Khalid says: This is the best day of the week!"),
], q=[
    ("mc", "متى يذهب خالد إلى السوق؟", "When does Khalid go to the market?",
     ["يوم السبت", "يوم الجمعة", "يوم الأحد", "يوم الاثنين"], ["السبت", "سوق"], 0),
    ("tf", "التفاح غال اليوم.", "Apples are expensive today.", False, ["تفاح", "رخيص"], 4),
    ("tf", "خالد لا يحب الفاكهة.", "Khalid doesn't like fruit.", False, ["أحب", "فاكهة"], 3),
    ("mc", "كيف يعود خالد وأمه إلى البيت؟", "How do Khalid and his mother get home?",
     ["في الحافلة", "في السيارة", "في القطار", "على الدراجة"], ["عاد", "حافلة"], 6),
]))

P.append(dict(title="رسالة إلى سارة", names=["سارة", "هند", "ليلى", "مريم", "فاطمة"], s=[
    ("مرحبا يا سارة!", "Hi, Sara!"),
    ("أنا الآن في المدينة الجديدة مع أبي وأمي.", "I am now in the new city with my father and mother."),
    ("بيتنا الجديد جميل وله حديقة كبيرة.", "Our new house is beautiful and has a big garden."),
    ("غرفتي صغيرة، لكن فيها نافذة كبيرة.", "My room is small, but it has a big window."),
    ("أبي يعمل الآن في شركة كبيرة هنا.", "My father now works for a big company here."),
    ("المدرسة الجديدة قريبة من البيت، فأذهب إليها كل يوم مع أخي.",
     "The new school is near the house, so I go there every day with my brother."),
    ("عندي صديقة جديدة اسمها هند.", "I have a new friend called Hind."),
    ("يوم الأحد ذهبنا إلى البحر، وكان الماء باردا جدا.", "On Sunday we went to the sea, and the water was very cold."),
    ("لكنك صديقتي الأولى دائما.", "But you are always my first friend."),
    ("اكتبي لي رسالة قريبا!", "Write me a letter soon!"),
    ("مع السلامة، ليلى.", "Goodbye, Laila."),
], q=[
    ("tf", "بيت ليلى الجديد ليس له حديقة.", "Laila's new house has no garden.", False, ["بيت", "حديقة"], 2),
    ("mc", "ما اسم صديقة ليلى الجديدة؟", "What is the name of Laila's new friend?",
     ["هند", "سارة", "مريم", "فاطمة"], ["صديق", "جديد"], 6),
    ("tf", "كان ماء البحر باردا جدا.", "The sea water was very cold.", True, ["ماء", "بارد"], 7),
    ("mc", "أين يعمل أبو ليلى الآن؟", "Where does Laila's father work now?",
     ["في شركة", "في مدرسة", "في مستشفى", "في مطعم"], ["عمل", "شركة"], 4),
]))

P.append(dict(title="الفصول الأربعة", names=[], s=[
    ("في بلدنا أربعة فصول.", "In our country there are four seasons."),
    ("في الشتاء يكون الهواء باردا، والمطر كثير.", "In winter the air is cold, and there is a lot of rain."),
    ("في الربيع تصبح الحديقة جميلة، والأشجار خضراء.", "In spring the garden becomes beautiful, and the trees are green."),
    ("الصيف حار جدا، فنذهب إلى البحر.", "Summer is very hot, so we go to the sea."),
    ("في الخريف نعود إلى المدرسة.", "In autumn we go back to school."),
    ("أنا أحب الربيع أكثر من كل الفصول، لأن الشمس جميلة والهواء ليس باردا.",
     "I like spring more than all the seasons, because the sun is lovely and the air is not cold."),
    ("أما أخي فيحب الشتاء، لأنه يحب المطر.", "As for my brother, he likes winter, because he likes the rain."),
    ("في الشتاء نجلس في البيت ونشرب الشاي الحار.", "In winter we sit at home and drink hot tea."),
    ("وأمي تحب الخريف، لأن الهواء ليس حارا ولا باردا.", "And my mother likes autumn, because the air is neither hot nor cold."),
], q=[
    ("mc", "ماذا تفعل العائلة في الصيف؟", "What does the family do in summer?",
     ["تذهب إلى البحر", "تبقى في البيت", "تذهب إلى الجبل", "تعود إلى المدرسة"], ["صيف", "بحر"], 3),
    ("tf", "الكاتب يحب الشتاء أكثر من كل الفصول.", "The writer likes winter more than all the seasons.", False,
     ["أحب", "ربيع"], 5),
    ("tf", "أخو الكاتب يحب المطر.", "The writer's brother likes the rain.", True, ["أخ", "مطر"], 6),
    ("mc", "متى يعود الأطفال إلى المدرسة؟", "When do the children go back to school?",
     ["في الخريف", "في الربيع", "في الشتاء", "في الصيف"], ["خريف", "مدرسة"], 4),
]))

P.append(dict(title="في المطعم", names=["يوسف"], s=[
    ("ذهبت مع صديقي يوسف إلى مطعم جديد في شارعنا.", "I went with my friend Yousef to a new restaurant on our street."),
    ("المطعم صغير، لكنه جميل جدا.", "The restaurant is small, but it is very nice."),
    ("طلبت اللحم والرز، وطلب يوسف السمك.", "I ordered meat and rice, and Yousef ordered fish."),
    ("شربنا الماء البارد.", "We drank cold water."),
    ("كان الطعام جيدا جدا.", "The food was very good."),
    ("بعد الطعام شربنا القهوة.", "After the meal we drank coffee."),
    ("كان الحساب ثلاثين دولارا فقط، فدفعه يوسف.", "The bill was only thirty dollars, and Yousef paid it."),
    ("في المرة القادمة سأدفع أنا.", "Next time I will pay."),
    ("المطعم قريب من بيتي، في شارع صغير.", "The restaurant is near my house, on a small street."),
    ("يوسف يحب هذا المطعم كثيرا، ويقول إن السمك فيه جيد جدا.", "Yousef likes this restaurant a lot, and he says the fish there is very good."),
], q=[
    ("mc", "ماذا طلب يوسف؟", "What did Yousef order?",
     ["سمكا", "لحما", "رزا", "خبزا"], ["طلب", "سمك"], 2),
    ("tf", "المطعم كبير جدا.", "The restaurant is very big.", False, ["مطعم", "صغير"], 1),
    ("tf", "دفع يوسف الحساب.", "Yousef paid the bill.", True, ["دفع", "حساب"], 6),
    ("mc", "كم كان الحساب؟", "How much was the bill?",
     ["ثلاثين دولارا", "ثلاثة دولارات", "مئة دولار", "عشرين دولارا"], ["حساب", "دولار"], 6),
]))

P.append(dict(title="كلبي", names=["بوبي"], s=[
    ("عندي كلب صغير اسمه بوبي.", "I have a small dog called Bobby."),
    ("بوبي كلب أبيض وجميل.", "Bobby is a white and beautiful dog."),
    ("يحب بوبي أن يلعب في الحديقة مع الأطفال.", "Bobby likes to play in the garden with the children."),
    ("في الصباح أعطيه الطعام والماء.", "In the morning I give him food and water."),
    ("ثم نخرج إلى الشارع قبل المدرسة.", "Then we go out into the street before school."),
    ("بوبي لا يحب القطط، ولا يحب الماء أيضا.", "Bobby doesn't like cats, and he doesn't like water either."),
    ("في المساء ينام في غرفتي، بجانب سريري.", "In the evening he sleeps in my room, next to my bed."),
    ("هو صديقي الأول.", "He is my best friend."),
    ("يوم الجمعة يذهب بوبي معنا إلى البحر، لكنه لا يدخل الماء.", "On Friday Bobby goes with us to the sea, but he doesn't go into the water."),
    ("كل الناس في شارعنا يعرفون بوبي ويحبونه.", "Everyone on our street knows Bobby and loves him."),
], q=[
    ("mc", "ما لون بوبي؟", "What colour is Bobby?",
     ["لونه أبيض", "لونه أسود", "لونه بني", "لونه رمادي"], ["أبيض"], 1),
    ("tf", "بوبي يحب الماء.", "Bobby likes water.", False, ["أحب", "ماء"], 5),
    ("tf", "ينام بوبي في غرفة الكاتب.", "Bobby sleeps in the writer's room.", True, ["نام", "غرفة"], 6),
    ("mc", "مع من يلعب بوبي في الحديقة؟", "Who does Bobby play with in the garden?",
     ["مع الأطفال", "مع القطط", "مع كلب آخر", "مع أم الكاتب"], ["لعب", "طفل"], 2),
]))

P.append(dict(title="إلى كل الطلاب", names=[], s=[
    ("إلى كل الطلاب:", "To all students:"),
    ("غدا الأربعاء لا توجد دروس في المدرسة.", "Tomorrow, Wednesday, there are no lessons at school."),
    ("كل المعلمين عندهم عمل في الجامعة.", "All the teachers have work at the university."),
    ("يوم الخميس تبدأ الدروس في الساعة 8.", "On Thursday lessons begin at 8 o'clock."),
    ("لا تنسوا كتبكم وأقلامكم يوم الخميس.", "Don't forget your books and pens on Thursday."),
    ("الطالب الذي لا يأتي يوم الخميس يجب أن يعطي المعلم رسالة من أبيه أو أمه.",
     "A student who does not come on Thursday must give the teacher a letter from his father or mother."),
    ("الدرس الأول يوم الخميس درس اللغة.", "The first lesson on Thursday is the language lesson."),
    ("بعد الدروس يلعب الطلاب في الحديقة حتى الساعة الثالثة.", "After lessons the students play in the garden until three o'clock."),
    ("شكرا، المدرسة.", "Thank you. The school."),
], q=[
    ("tf", "لا توجد دروس يوم الأربعاء.", "There are no lessons on Wednesday.", True, ["الأربعاء", "درس"], 1),
    ("mc", "لماذا لا توجد دروس غدا؟", "Why are there no lessons tomorrow?",
     ["لأن المعلمين في الجامعة", "لأن اليوم عيد", "لأن المعلم الجديد مريض جدا", "لأن الطلاب في البحر"], ["معلم"], 2),
    ("tf", "يجب على كل الطلاب أن يعطوا المعلم رسالة.", "All students must give the teacher a letter.", False, ["رسالة"], 5),
    ("mc", "ماذا يجب ألا ينسى الطلاب يوم الخميس؟", "What must students not forget on Thursday?",
     ["كتبهم", "طعامهم", "صورهم", "ساعاتهم"], ["نسي", "كتاب"], 4),
    ("mc", "متى تبدأ الدروس يوم الخميس؟", "When do lessons begin on Thursday?",
     ["في الساعة 8", "في الساعة 3", "في الساعة 10", "في المساء"], ["بدأ", "ساعة"], 3),
]))

P.append(dict(title="عيد ميلاد منى", names=["منى"], s=[
    ("اليوم عيد ميلاد أختي منى.", "Today is my sister Mona's birthday."),
    ("عمرها اليوم عشرون سنة.", "Today she is twenty years old."),
    ("في المساء جاء أصدقاؤها إلى بيتنا.", "In the evening her friends came to our house."),
    ("أمي وضعت على الطاولة طعاما كثيرا، وأبي اشترى لها هدية.",
     "My mother put a lot of food on the table, and my father bought her a present."),
    ("كانت الهدية ساعة حمراء صغيرة.", "The present was a small red watch."),
    ("أنا أعطيتها كتابا، لأنها تحب الكتب.", "I gave her a book, because she loves books."),
    ("أكلنا وشربنا وتكلمنا كثيرا.", "We ate, drank and talked a lot."),
    ("قالت منى: هذا يوم رائع!", "Mona said: This is a wonderful day!"),
    ("كانت منى سعيدة جدا.", "Mona was very happy."),
    ("بعد العشاء شربنا الشاي والقهوة، وأكلنا الفاكهة.", "After dinner we drank tea and coffee, and ate fruit."),
    ("ثم ذهب أصدقاؤها إلى بيوتهم، ونامت منى سعيدة.", "Then her friends went to their homes, and Mona went to sleep happy."),
], q=[
    ("mc", "كم عمر منى اليوم؟", "How old is Mona today?",
     ["عشرون سنة", "عشر سنوات", "ثلاثون سنة", "خمس عشرة سنة"], ["عمر", "عشرون"], 1),
    ("tf", "اشترى الأب لمنى هدية.", "The father bought Mona a present.", True, ["أب", "اشترى"], 3),
    ("tf", "أعطى الكاتب منى ساعة حمراء.", "The writer gave Mona a red watch.", False, ["أعطى", "كتاب"], 5),
    ("mc", "من جاء إلى البيت في المساء؟", "Who came to the house in the evening?",
     ["أصدقاء منى", "أسرة الأب", "معلمو منى", "الجيران"], ["مساء", "صديق"], 2),
]))

P.append(dict(title="بيتنا الجديد", names=[], s=[
    ("في الشهر الماضي بدأنا نسكن في بيت جديد.", "Last month we started living in a new house."),
    ("البيت كبير، وفيه أربع غرف ومطبخ وحمام.", "The house is big, and it has four rooms, a kitchen and a bathroom."),
    ("في الغرفة الكبيرة كرسيان وطاولة.", "In the big room there are two chairs and a table."),
    ("غرفتي فوق المطبخ.", "My room is above the kitchen."),
    ("فيها سرير ومكتب صغير ونافذة كبيرة.", "It has a bed, a small desk and a big window."),
    ("من النافذة أرى الحديقة والأشجار.", "From the window I see the garden and the trees."),
    ("أمي تحب المطبخ، لأن فيه نافذتين.", "My mother likes the kitchen, because it has two windows."),
    ("أبي يقول إن البيت غال قليلا، لكننا سعداء فيه.", "My father says the house is a little expensive, but we are happy in it."),
    ("في الحديقة شجرة كبيرة، وتحتها كرسي.", "In the garden there is a big tree, and under it a chair."),
    ("أنا أجلس هناك كل يوم وأقرأ كتابا.", "I sit there every day and read a book."),
    ("بيتنا قريب من مدرستي ومن السوق.", "Our house is near my school and the market."),
], q=[
    ("mc", "كم غرفة في البيت الجديد؟", "How many rooms are in the new house?",
     ["أربع غرف", "غرفتان", "ثلاث غرف", "خمس غرف"], ["غرفة"], 1),
    ("tf", "غرفة الكاتب فوق المطبخ.", "The writer's room is above the kitchen.", True, ["غرفة", "مطبخ"], 3),
    ("tf", "ليس في غرفة الكاتب نافذة.", "There is no window in the writer's room.", False, ["نافذة"], 4),
    ("mc", "ماذا يقول الأب عن البيت؟", "What does the father say about the house?",
     ["إنه غال قليلا", "إنه صغير جدا", "إنه قديم جدا", "إنه بعيد جدا عن البيت"], ["قال", "غال"], 7),
]))

P.append(dict(title="الجمعة في الحديقة", names=[], s=[
    ("يوم الجمعة يذهب الناس إلى الحديقة الكبيرة في مدينتنا.", "On Friday people go to the big park in our city."),
    ("الأطفال يلعبون بالكرة، والكبار يجلسون تحت الأشجار.", "The children play ball, and the grown-ups sit under the trees."),
    ("بعض الناس يأكلون ويشربون الشاي.", "Some people eat and drink tea."),
    ("أنا أذهب إلى هناك مع أبي وأخي الصغير.", "I go there with my father and my little brother."),
    ("أبي يقرأ كتابا، وأنا ألعب مع أخي.", "My father reads a book, and I play with my brother."),
    ("في المساء نشتري الخبز ونعود إلى البيت.", "In the evening we buy bread and go back home."),
    ("أنا أحب يوم الجمعة كثيرا.", "I like Friday very much."),
    ("بعض الأطفال يأكلون الفاكهة، وبعضهم يشربون الحليب.", "Some children eat fruit, and some of them drink milk."),
    ("أمي لا تأتي معنا، لأنها تعمل في المستشفى يوم الجمعة.", "My mother doesn't come with us, because she works at the hospital on Fridays."),
], q=[
    ("tf", "الأب يقرأ كتابا في الحديقة.", "The father reads a book in the park.", True, ["أب", "قرأ"], 4),
    ("mc", "ماذا يفعل الأطفال في الحديقة؟", "What do the children do in the park?",
     ["يلعبون بالكرة", "يقرؤون الكتب", "يشربون الشاي في البيت", "ينامون"], ["طفل", "لعب"], 1),
    ("tf", "يذهب الكاتب إلى الحديقة مع أمه.", "The writer goes to the park with his mother.", False, ["ذهب", "أب"], 3),
    ("mc", "ماذا تشتري العائلة في المساء؟", "What does the family buy in the evening?",
     ["خبزا", "شايا", "كتابا", "كرة"], ["اشترى", "خبز"], 5),
]))

P.append(dict(title="أول يوم في العمل", names=["طارق", "رنا"], s=[
    ("اليوم أول يوم لي في العمل الجديد.", "Today is my first day at the new job."),
    ("أعمل في مكتب شركة كبيرة في المدينة.", "I work in the office of a big company in the city."),
    ("وصلت في الساعة 8، وكان المدير هناك.", "I arrived at 8 o'clock, and the manager was there."),
    ("قال لي: أهلا بك في شركتنا!", "He said to me: Welcome to our company!"),
    ("ثم أعطاني مكتبا صغيرا بجانب النافذة.", "Then he gave me a small desk next to the window."),
    ("في الغداء أكلت مع رجل اسمه طارق وامرأة اسمها رنا.", "At lunch I ate with a man called Tariq and a woman called Rana."),
    ("هما لطيفان جدا، وساعداني كثيرا.", "They are very kind, and they helped me a lot."),
    ("في المساء عدت إلى البيت سعيدا.", "In the evening I went back home happy."),
    ("كان العمل سهلا في اليوم الأول.", "The work was easy on the first day."),
    ("غدا يبدأ العمل الحقيقي!", "Tomorrow the real work begins!"),
], q=[
    ("tf", "كان المدير في الشركة عندما وصل الكاتب.", "The manager was at the company when the writer arrived.", True,
     ["مدير", "وصل"], 2),
    ("mc", "أين مكتب الكاتب؟", "Where is the writer's desk?",
     ["قريب من النافذة", "قريب من الباب", "قريب من المدير", "قريب من باب المطبخ"], ["مكتب", "نافذة"], 4),
    ("tf", "أكل الكاتب الغداء مع المدير.", "The writer ate lunch with the manager.", False, ["أكل", "غداء"], 5),
    ("mc", "كيف كان الكاتب في المساء؟", "How was the writer in the evening?",
     ["كان سعيدا", "كان حزينا", "كان مريضا", "كان جائعا"], ["عاد", "سعيد"], 7),
]))

P.append(dict(title="أين المستشفى؟", names=["علي"], s=[
    ("سأل رجل في الشارع: من فضلك، أين المستشفى؟", "A man in the street asked: Excuse me, where is the hospital?"),
    ("قال له علي: المستشفى ليس بعيدا من هنا.", "Ali said to him: The hospital is not far from here."),
    ("اذهب في هذا الشارع حتى الفندق الكبير، ثم خذ الشارع الثاني.",
     "Go along this street as far as the big hotel, then take the second street."),
    ("بعد خمس دقائق ترى مدرسة كبيرة.", "After five minutes you see a big school."),
    ("المستشفى أمام المدرسة، بجانب محطة الحافلات.", "The hospital is opposite the school, next to the bus station."),
    ("سأل الرجل: هل أستطيع أن أذهب إلى هناك بدون سيارة؟", "The man asked: Can I get there without a car?"),
    ("قال علي: نعم، الطريق قريب.", "Ali said: Yes, it is not far."),
    ("قال الرجل: شكرا جزيلا!", "The man said: Thank you very much!"),
    ("ثم ذهب الرجل في الطريق إلى المستشفى.", "Then the man went on his way to the hospital."),
], q=[
    ("tf", "المستشفى بعيد جدا.", "The hospital is very far.", False, ["بعيد", "مستشفى"], 1),
    ("mc", "أين المستشفى؟", "Where is the hospital?",
     ["أمام المدرسة", "بجانب الفندق", "أمام البيت", "في الشارع الأول"], ["مستشفى", "أمام"], 4),
    ("tf", "يستطيع الرجل أن يذهب إلى المستشفى بدون سيارة.", "The man can get to the hospital without a car.", True,
     ["طريق", "قريب"], 6),
    ("mc", "ماذا يرى الرجل بعد خمس دقائق؟", "What does the man see after five minutes?",
     ["مدرسة كبيرة", "فندقا كبيرا", "محطة القطار", "مستشفى صغيرا"], ["رأى", "مدرسة"], 3),
]))

P.append(dict(title="قطة الجيران", names=[], s=[
    ("لجيراننا قطة صغيرة رمادية.", "Our neighbours have a small grey cat."),
    ("كل صباح تأتي القطة إلى حديقتنا.", "Every morning the cat comes to our garden."),
    ("تجلس تحت الشجرة وتنام في الشمس.", "She sits under the tree and sleeps in the sun."),
    ("أمي لا تحب القطط، لكن أختي تحبها كثيرا.", "My mother doesn't like cats, but my sister loves her."),
    ("أختي تعطيها الحليب في الصباح.", "My sister gives her milk in the morning."),
    ("في يوم من الأيام لم تأت القطة، فكانت أختي حزينة.", "One day the cat did not come, and my sister was sad."),
    ("في المساء ذهبنا إلى بيت الجيران.", "In the evening we went to the neighbours' house."),
    ("قالوا إن القطة مريضة، وهي الآن عند الطبيب.", "They said the cat was ill, and she was at the vet's now."),
    ("بعد ثلاثة أيام عادت القطة إلى حديقتنا، وكانت أختي سعيدة جدا.",
     "Three days later the cat came back to our garden, and my sister was very happy."),
], q=[
    ("mc", "ماذا تعطي الأخت القطة؟", "What does the sister give the cat?",
     ["حليبا", "لحما", "ماء", "خبزا"], ["أعطى", "حليب"], 4),
    ("tf", "أم الكاتب تحب القطط.", "The writer's mother likes cats.", False, ["أم", "أحب"], 3),
    ("tf", "كانت القطة مريضة.", "The cat was ill.", True, ["مريض"], 7),
    ("mc", "متى عادت القطة؟", "When did the cat come back?",
     ["بعد ثلاثة أيام", "بعد يوم واحد", "بعد أسبوع واحد", "بعد شهر"], ["عاد"], 8),
]))

P.append(dict(title="رسالة من الإسكندرية", names=["الإسكندرية", "القاهرة", "يوسف"], s=[
    ("أمي العزيزة،", "Dear Mum,"),
    ("أنا الآن في الإسكندرية مع أصدقائي من الجامعة.", "I am now in Alexandria with my friends from the university."),
    ("الفندق صغير لكنه قريب من البحر.", "The hotel is small but it is near the sea."),
    ("كل يوم نذهب إلى البحر، ونأكل السمك في مطعم.", "Every day we go to the sea, and we eat fish in a restaurant."),
    ("الجو هنا حار في الصباح، لكنه جميل في المساء.", "The weather here is hot in the morning, but it is lovely in the evening."),
    ("أمس ذهبنا إلى مكان قديم وأخذنا صورا كثيرة.", "Yesterday we went to an old place and took a lot of pictures."),
    ("سنعود إلى القاهرة يوم الأحد بالقطار.", "We will go back to Cairo on Sunday by train."),
    ("المدينة جميلة جدا، وفيها أماكن كثيرة.", "The city is very beautiful, and there are many places in it."),
    ("أنا بخير، وكيف حالك أنت وأبي؟", "I am well. How are you and Dad?"),
    ("ابنك، يوسف.", "Your son, Yousef."),
], q=[
    ("mc", "أين الفندق؟", "Where is the hotel?",
     ["بجانب البحر", "بعيد عن البحر", "بجانب المطعم", "بجانب الجامعة"], ["فندق", "قريب"], 2),
    ("tf", "يأكل يوسف وأصدقاؤه السمك.", "Yousef and his friends eat fish.", True, ["أكل", "سمك"], 3),
    ("tf", "سيعود يوسف إلى القاهرة بالحافلة.", "Yousef will go back to Cairo by bus.", False, ["عاد", "قطار"], 6),
    ("mc", "ماذا فعل يوسف وأصدقاؤه أمس؟", "What did Yousef and his friends do yesterday?",
     ["أخذوا صورا", "ذهبوا إلى السوق", "رجعوا إلى البيت", "كتبوا رسائل"], ["أخذ", "صورة"], 5),
]))

P.append(dict(title="الأم على الهاتف", names=[], s=[
    ("اتصلت بي أمي أمس في المساء.", "My mother called me yesterday evening."),
    ("سألتني: كيف حالك؟ هل تأكل جيدا؟", "She asked me: How are you? Are you eating well?"),
    ("قلت لها: أنا بخير، وآكل في مطعم الجامعة كل يوم.", "I told her: I'm fine, and I eat at the university restaurant every day."),
    ("قالت: لا تعمل كثيرا بعد العشاء.", "She said: Don't work too much after dinner."),
    ("ثم تكلمت مع أبي.", "Then I talked with my father."),
    ("أبي قال إنه سيأتي إلى مدينتي في الشهر القادم.", "My father said he would come to my city next month."),
    ("أنا سعيد جدا، لأني لم أر أبي منذ ثلاثة أشهر.", "I am very happy, because I haven't seen my father for three months."),
    ("أنا أيضا أريد أن أرى أمي وأختي الصغيرة.", "I also want to see my mother and my little sister."),
    ("سأذهب إلى البيت في الصيف، بعد نهاية الدروس.", "I will go home in the summer, after the end of lessons."),
], q=[
    ("tf", "اتصلت الأم بالكاتب في الصباح.", "The mother called the writer in the morning.", False, ["اتصل", "مساء"], 0),
    ("mc", "أين يأكل الكاتب كل يوم؟", "Where does the writer eat every day?",
     ["في الجامعة", "في البيت", "عند صديقه", "في المستشفى"], ["أكل", "جامعة"], 2),
    ("tf", "سيأتي الأب في الشهر القادم.", "The father will come next month.", True, ["أتى", "شهر"], 5),
    ("mc", "منذ متى لم ير الكاتب أباه؟", "How long has it been since the writer saw his father?",
     ["منذ ثلاثة أشهر", "منذ أسبوع", "منذ شهر", "منذ أسبوعين فقط"], ["أب", "منذ"], 6),
]))

P.append(dict(title="في درس اللغة", names=["ماريا", "فاطمة", "القاهرة", "اليابان"], s=[
    ("اسمي ماريا، وأنا طالبة أمريكية في القاهرة.", "My name is Maria, and I am an American student in Cairo."),
    ("أدرس اللغة العربية كل يوم من الأحد إلى الخميس.", "I study Arabic every day from Sunday to Thursday."),
    ("في الدرس عشرة طلاب من بلاد مختلفة.", "There are ten students from different countries in the class."),
    ("معلمتنا اسمها فاطمة، وهي معلمة جيدة جدا.", "Our teacher is called Fatima, and she is a very good teacher."),
    ("في الدرس نقرأ ونكتب ونتكلم كثيرا.", "In class we read, write and talk a lot."),
    ("أنا أتكلم جيدا، لكني لا أكتب جيدا.", "I speak well, but I don't write well."),
    ("بعد الدرس أشرب القهوة مع صديقتي من اليابان.", "After class I drink coffee with my friend from Japan."),
    ("هي تتكلم العربية جيدا جدا.", "She speaks Arabic very well."),
    ("في المساء أقرأ كتبا سهلة وأشاهد أفلاما عربية.", "In the evening I read easy books and watch Arabic films."),
], q=[
    ("mc", "ماذا تدرس ماريا في القاهرة؟", "What does Maria study in Cairo?",
     ["اللغة العربية", "الموسيقى", "التاريخ", "القانون"], ["درس", "لغة"], 1),
    ("tf", "في الدرس عشرون طالبا.", "There are twenty students in the class.", False, ["طالب", "عشرة"], 2),
    ("tf", "ماريا لا تكتب جيدا.", "Maria doesn't write well.", True, ["كتب", "جيد"], 5),
    ("mc", "ماذا تفعل ماريا بعد الدرس؟", "What does Maria do after class?",
     ["تشرب القهوة مع صديقتها", "تعود إلى البيت مع أختها", "تكتب رسالة إلى أمها", "تذهب إلى السوق مع معلمتها"],
     ["شرب", "قهوة"], 6),
]))

P.append(dict(title="في القطار", names=["القاهرة", "الإسكندرية"], s=[
    ("أنا الآن في القطار من القاهرة إلى الإسكندرية.", "I am now on the train from Cairo to Alexandria."),
    ("القطار ليس سريعا، لكنه جميل.", "The train is not fast, but it is nice."),
    ("بجانبي رجل كبير يقرأ كتابا قديما.", "Next to me an old man is reading an old book."),
    ("أمامي امرأة مع طفلين صغيرين.", "In front of me there is a woman with two small children."),
    ("الطفلان يأكلان الخبز وينظران من النافذة.", "The two children are eating bread and looking out of the window."),
    ("من النافذة أرى الأرض الخضراء والبيوت الصغيرة.", "From the window I see the green land and the small houses."),
    ("الطريق ثلاث ساعات فقط.", "The journey is only three hours."),
    ("أقرأ كتابي، ثم أنام حتى نصل.", "I read my book, then I sleep until we arrive."),
    ("في القطار مطعم صغير، فأشتري منه قهوة وخبزا.", "There is a small restaurant on the train, so I buy coffee and bread from it."),
    ("نصل إلى الإسكندرية في الساعة الثالثة.", "We arrive in Alexandria at three o'clock."),
], q=[
    ("tf", "القطار سريع جدا.", "The train is very fast.", False, ["قطار", "سريع"], 1),
    ("mc", "ماذا يفعل الرجل الكبير؟", "What is the old man doing?",
     ["يقرأ", "ينام", "يأكل الخبز", "ينظر من النافذة"], ["رجل", "قرأ"], 2),
    ("tf", "مع المرأة طفلان.", "The woman has two children with her.", True, ["امرأة", "طفل"], 3),
    ("mc", "متى يصل القطار إلى الإسكندرية؟", "When does the train arrive in Alexandria?",
     ["في الساعة الثالثة", "في الساعة الأولى", "في الساعة الثانية", "في المساء"], ["وصل", "ساعة"], 9),
]))

P.append(dict(title="طعام من بلدنا", names=[], s=[
    ("هذا طعام سهل تستطيع أن تعمله في البيت.", "This is an easy dish you can make at home."),
    ("تحتاج رزا ولحما وماء.", "You need rice, meat and water."),
    ("أولا، ضع اللحم في الماء مدة ساعة.", "First, put the meat in the water for an hour."),
    ("ثم ضع الرز مع اللحم.", "Then put the rice with the meat."),
    ("بعد عشرين دقيقة يصبح الطعام جاهزا.", "After twenty minutes the food is ready."),
    ("يمكن أن تأكله مع الخبز.", "You can eat it with bread."),
    ("هو طعام رخيص وجيد للأطفال.", "It is a cheap dish and good for children."),
    ("أمي تعمل هذا الطعام كل يوم جمعة، وكل الأسرة تحبه.", "My mother makes this dish every Friday, and the whole family loves it."),
    ("الكبار والصغار يأكلون منه كثيرا.", "Grown-ups and children eat a lot of it."),
    ("في المرة القادمة سأعمله أنا لأصدقائي.", "Next time I will make it for my friends."),
], q=[
    ("mc", "ماذا تضع أولا في الماء؟", "What do you put in the water first?",
     ["اللحم", "الرز", "الخبز", "الحليب"], ["وضع", "لحم"], 2),
    ("tf", "يصبح الطعام جاهزا بعد ساعتين.", "The food is ready after two hours.", False, ["أصبح", "دقيقة"], 4),
    ("tf", "هذا الطعام غال.", "This dish is expensive.", False, ["رخيص", "طعام"], 6),
    ("mc", "متى تعمل الأم هذا الطعام؟", "When does the mother make this dish?",
     ["مرة في الأسبوع", "مرة في الشهر", "كل صباح", "مرة واحدة في السنة"], ["عمل", "طعام"], 7),
    ("tf", "يمكن أن تأكل هذا الطعام مع الخبز.", "You can eat this dish with bread.", True, ["أمكن", "خبز"], 5),
]))

P.append(dict(title="صديق جديد", names=["مازن", "سوريا"], s=[
    ("في المدرسة طالب جديد اسمه مازن.", "There is a new student at school called Mazen."),
    ("هو من سوريا، وجاء مع أسرته إلى بلدنا هذا العام.", "He is from Syria, and he came to our country with his family this year."),
    ("في اليوم الأول كان مازن وحيدا ولا يتكلم مع أحد.", "On the first day Mazen was alone and didn't talk to anyone."),
    ("جلست بجانبه وقلت له: ما اسمك؟ ومن أين أنت؟", "I sat next to him and said to him: What's your name? And where are you from?"),
    ("قال لي إنه يحب كرة القدم.", "He told me he loves football."),
    ("أنا أيضا أحب كرة القدم!", "I love football too!"),
    ("بعد المدرسة لعبت معه في الشارع.", "After school I played with him in the street."),
    ("الآن مازن صديقي، ونلعب كل يوم بعد الدروس.", "Now Mazen is my friend, and we play every day after lessons."),
    ("أبوه طبيب، وأمه معلمة في مدرستنا.", "His father is a doctor, and his mother is a teacher at our school."),
], q=[
    ("mc", "ماذا يحب مازن؟", "What does Mazen love?",
     ["كرة القدم", "الموسيقى", "الكتب", "القطط"], ["أحب"], 4),
    ("tf", "كان مازن سعيدا جدا في اليوم الأول.", "Mazen was very happy on the first day.", False, ["أول", "وحيد"], 2),
    ("tf", "أم مازن طبيبة.", "Mazen's mother is a doctor.", False, ["أم", "طبيب"], 8),
    ("tf", "يلعب مازن مع الكاتب بعد الدروس.", "Mazen plays with the writer after lessons.", True, ["لعب", "درس"], 7),
]))
