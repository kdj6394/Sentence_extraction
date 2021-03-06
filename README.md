# Sentence_extraction

## 개요
[Dacon](https://dacon.io/competitions/official/235671/overview/) 에서 주관하는 한국어 문서 추출요약 AI 경진대회의 데이터를 이용하여 요약추출을 시도한다.

## 순서
1. 데이터 확인
2. Textrank

## requirements
* pip install -r requiremets.txt
* [KoNLPy](https://konlpy.org/ko/latest/install/)

## path
* train_data_refine path : User\data\data
* abstractive : User\data\data

## Report
### 데이터 확인

* 데이터 구성  
* train.jsonl - 학습에 사용될 데이터셋  
1. media : 기사 미디어
2. id : 각 데이터 고유번호
3. article_original : 전체 기사 내용, 문장별로 split되어 있음
4. abstractive : 사람이 생성한 요약문
5. extractive : 사람이 추출한 요약문 3개의 index

* extractive_test.jsonl - 추론할 데이터셋  
1. media : 기사 미디어
2. id : 각 데이터 고유 번호
3. article_original : 전체 기사 내용, 문장별로 split되어 있음

* train.jsonl 데이터 중 원문(article_original) 만 사용하기위해 원문(article_original)의 데이터만 article_original.txt 로 재저장함.


### Textrank
* textrank 테스트 결과는 아래와 같다. 

    article :  '당진시 문화관광과를 대상으로 하는 행정사무감사에서 당진시립합창단 관계자가 보낸 것으로 추정되는 문자와 관련 해 당진시의회가 행정사무조사특별위원회를 구성해 조사하겠다고 밝혔다.', '당진시의회 행정사무감사 3일차였던 지난 6일 문화 관광과를 대상으로 하는 행감에서 최창용 의원은 “(당진시립합창단 정기연주회를 앞두고) 문자메세지를 제보받았다”며 “(음향팀에 보낸 것으로 추정되는) 해당 문자에는 ‘합창단이 소리를 작게 낼 것이니 알고 있으라’는 내용이었다”고 말했다.', '이어 “공연에서 소리를 작게 낸다는 것은 합창단으로서 그 임무를 하지 않겠다는 것”이며 “공연 자체를 무력화해 당진시를 망신  주려는 행위”라며 해당 문자를 보낸 단원 등 연루된 사람들을 찾아 사실관계를 확인하고 징계 등 책임을 물어야 한다고 지적했 다.', '문제의 문자메세지를 전달받은 문화관광과는 감사법무담당관에게 조사를 의뢰했다.', '권경선 문화관광과장은 “누가, 어떻게 해서 해당 문자가 나온 것인지 정확히 조사해봐야 알 수 있다”며 “전달받은 문자 내용도 최 의원이 언급한 부분만 있어, 중간 내용만을 가지고는 전체를 유추할 수 없다”고 전했다.', '하지만 감사법무담당관실에서 아직 조사가 이뤄지지 않고 있어  당진시가 사태의 심각성을 인지하지 못하고 있다는 지적이다.', '그동안 행정사무감사가 진행되고 있어 사태를 지켜봤다던 감사 법무담당관실에서는 “관계된 사람들을 조사해 사태를 파악해야 하는데, 아직 조사에 대한 뚜렷한 계획이 없다”고 답했다.', ' 한편 행감이 끝난 지난 12일 당진시의회에서는 당진시립합창단 문제를 비롯해 구체적인 조사가 필요한 부분에 대해 행정사무조사특별위원회를 구성해 운영하겠다고 밝혔다.', '김기재 의장은 “본회의 의결과 제적의원 1/3의 발의가 있으면 행정사무조사특별 위원회를 구성할 수 있다”며 “다음 달 초 위원들과 상의해 위원회를 구성한다면 당진시립합창단 관련 사안을 비롯해 사회복지 기관 위수탁 등에 대해 다룰 계획”이라고 말했다.'

    summarize_0 ' 당 진시 문화관광과를 대상으로 하는 행정 사무감사에서 당 진 시립 합창단 관계자가 보낸 것으로 추정되는 문자 와 관련해 당 진시의회가 행정 사무조사 특별위원회를 구성해 조사하겠다고 밝혔다.

    summarize_1

    summarize_2 ', ' 그동안 행정 사무감사가 진행되고 있어 사태를 지켜봤다 던 감사 법무 담당관 실에서는 “ 관계된 사람들을 조사해 사태를 파악해야 하는데, 아직 조사에 대한 뚜렷한 계획이 없다” 고 답했다.

    keywords :  ['합창단', '조사', '문자', '의원', '시립', '사무', '행정', '해당', '진시', '구성']

    article :  '미국 메이저리그(MLB)에서 활동하는 한국 선수들의 시즌 초반 희비가 엇갈리고 있다.', 'LA 에인절스의 최지만은 맹활약으로 주전 입지를 굳혀가는 반면 텍사스 레인저스의 추신수는 개막전 선발에서 밀려나는 수모를 당한 뒤에서도 좀처럼 반등 을 하지 못하고 있다.', '최지만은 2일(한국시간) 미국 플로리다주 세인트피터즈버그 트로피카나 필드에서 열린 2019 미국프로야구 메이저리그 콜로라도 로키스와 홈경기에 3번 타자 1루수로 선발 출전해 4타수 2안타를 치고 1득점을 올렸다.', '시즌 타율은 0.250에서 0.313(16타수 5안타)로 올랐다.', '최지만은 개막전에서 4타수 무안타로 침묵했으나 이후 3경기 연속 안타이자 2경기 연속 멀티 히트를 뽑아내며 입지를 굳혀갔다.', '2016년 LA 에인절스 소속으로 메이저리그에 데뷔한 최지만이 2경기 연속 멀티  히트를 친 것은 이번이 처음이다.', '스코어가 벌어진 탓에 콜로라도 불펜의 필승조인 오승환과 최지만의 맞대결은 성사되지 않 았다.', '추신수는 들쭉날쭉한 출전 일정 탓인지 타격감을 찾지 못하고 있다.', '추신수는 이날 텍사스주 알링턴 글로브 라이프 파크에서 열린 휴스턴 애스트로스와 홈경기에 1번 지명타자로 선발 출전했지만 4타수 무안타로 침묵했다.', '시즌 타율은 0.167 에서 0.100(10타수 1안타)로 떨어졌다.', '추신수는 11년 만에 개막전 선발 라인업에서 제외되는 등 이날까지 텍사스가 치른 4경기 가운데 2경기에만 선발 출전했다.', '크리스 우드워드 텍사스 감독은 상대 선발이 좌완이면 좌타자인 추신수 대신 우타자인  헌터 펜스를 선발 지명타자로 기용하고 있다.', '텍사스(2승 2패)는 휴스턴 마운드에 2안타로 꽁꽁 묶이며 1-2로 패해 2연승 행 진을 마감했다.', '한편 피츠버그 파이리츠의 강정호는 914일 만에 홈경기에 나섰지만 안타를 만들어내지 못했다.', '이날 펜실 베이니아주 피츠버그의 PNC 파크에서 열린 세인트루이스 카디널스와 홈 개막전에 선발 라인업에서 제외된 강정호는 벤치에서 경 기를 시작했다.', '강정호는 4-4 동점이 된 8회 초 2사 2루에서 3루 대수비로 교체 출전했다.', '강정호가 PNC 파크 그라운드를 다시 밟은 것은 2016년 9월 30일 시카고 컵스와의 홈 최종전 이후 정확히 914일 만이다.', '강정호는 8회 말 선두타자 모란이 솔로포를 터트려 스코어가 5-4가 된 이후 후속 타석에 들어섰지만 중견수 뜬공으로 물러났다.', '연장 10회 말 1사에서 다시 타석 에 들어선 강정호는 세인트루이스의 우완 ‘파이어볼러’ 조던 힉스에게 3구 삼진으로 물러났다.', '2타수 무안타 1삼진으로 침 묵한 강정호의 시즌 타율은 0.222(9타수 2안타)가 됐다.', '피츠버그는 연장 11회 혈투 끝에 5-6으로 패했다.'

    summarize_0 ', ' 추신 수는 이날 텍사스 주 알링턴 글로브 라이프 파크에서 열린 휴스턴 애스트로스와 홈경기에 1번 지명 타자 로 선발 출전했지만 4 타수 무안타로 침묵했다.

    summarize_1 ', ' 추신 수는 11년 만에 개막전 선발 라인업에서 제외되는 등 이날까지 텍사스가 치른 4 경기 가운데 2 경기에만 선발 출전했다.

    summarize_2 ', '2 타수 무안타 1 삼진으로 침묵한 강정 호의 시즌 타율은 0.222(9 타수 2 안 타) 가 됐다.

    keywords :  ['선발', '경기', '세인트', '출전', '텍사스', '타자', '안타', '메이저리그', '개막전', '파크']

    article :  '인천 부영공원 운영 생활야구협회 80여 동호회 팀에 260만 원씩 받아', '국유지로 임대료 없고 區서 지원도 일부 " 사용 내역 공개 등 폐쇄적"', '인천시 부평구 산곡동 부영공원 야구장을 운영하는 구 생활체육야구협회를 두고 특혜 논란이 불거지고 있다.', '사진은 부영공원 야구장 전경.', '김유리 기자 kyr@kihoilbo.co.kr', '인천시 부평구생활체육야구협회가 깜깜이로 부영공원을 운영하고 있다는 지적이 나오고 있다.', '16일 부평구와 협회 등에 따르면 부영공원 안에 있는 야구장을 구생활체육야구협회가 무상 사용하면서 이곳을 이용하는 야구동호회(80여 개 팀)로부터 팀별로 연간 260만 원씩 회비를 받고 있다.', '문제는 회비 산정 기준과 사용 내역이 투명하게 공개되지 않고 있다는 것이다.', '회비는 협회에서 주관하는 사회인 야구리그 운영  및 구장 관리에 사용된다.', '경기마다 심판 2명과 점수 기록원의 인건비 각 5만 원, 야구공 구입비, 구장 청소 비용 등으로 약 20만 원의 비용이 발생한다.', '일부 리그 회원들은 예결산 내역을 각 야구팀 감독들에게만 공개하는 등 폐쇄적으로 운영되고 있다고 지적했다.', '게다가 현금 사용이 많고 영수증 등 증빙자료가 없는 경우도 있어 신뢰하기 어렵다며 의혹을 제기했다.', '또 국유지를 임대료 없이 무상 사용하고 있고, 마사토 구입 등은 구 예산을 지원받는 협회가 회비까지 걷는 것은 지나친 특혜라는 주장이다.', '이들은 구가 직접 관리 주체가 되거나 공모 등을 통해 위탁운영을 정식으로 맡기기를 요구하고 있다.', '상황이 이런데도 구는 생활체육회에 관리·감독 권한을 행사할 수 없다는 이유로 방관하고 있다.', '현재 구생활체육회의 관리 권한은 인 천시생활체육회가 갖고 있는데다, 민간단체이기 때문에 사용 내역을 요구할 수 없다는 것이다.', '부평구생활체육협회 리그에 소속된 야구팀에서 활동하고 있는 A(46)씨는 "협회가 국유지를 공짜로 사용하면서 수익활동을 하고 있는데, 관리주체가 변한 적도 없고 현재 회장이 18년째 역임하고 있는 것은 형평성에 어긋난다"며 "야구공을 뺀 기타 용품은 개인이 준비하게 돼 있고, 시설이 제대로 관리되지 않는데 회비가 어떻게 사용되는지 알 방법이 없어 불만이 많이 나온다"고 주장했다.', '구 관계자는 "체육대회 등 구 보조금이 들어가는 사업을 할 때는 예결산 증빙을 요구하지만, 협회가 민간단체다 보니 회비 내역은 구에서 관리·감독하기가 어렵다"고 말했다.', '이에 대해 부평구생활체육야구협회 관계자는 "원래 미군 부대에서 사용하고 있던 공원부지를 야구장 으로 가꾸는 과정에서 우리 체육회의 공로가 있었기 때문에 관리 권한을 얻은 것"이라며 "내년부터는 투명하게 운영하기 위해 최근 법인통장도 만드는 등 노력하고 있다"고 했다.'

    summarize_0 ' 인천 부영공원 운영 생활야구협회 80 여 동호회 팀에 260만 원씩 받아', ' 국유지로 임대료 없고 區 서 지원도 일부 " 사용 내역 공개 등 폐쇄적"', ' 인천시 부평구 산곡동 부영공원 야구장을 운영하는 구 생활 체육야구협회를 두고 특혜 논란이 불거지고 있다.

    summarize_1 ', '16 일 부평구와 협회 등에 따르면 부영공원 안에 있는 야구장을 구 생활 체육야구협회가 무상 사용하면서 이곳 을 이용하는 야구 동호회 (80 여 개 팀 )로부터 팀 별로 연간 260만 원씩 회비를 받고 있다.

    summarize_2 ', ' 회비는 협회에서 주관하는 사회인 야구리그 운영 및 구장 관리에 사용된다.

    keywords :  ['사용', '협회', '부평구', '체육', '야구', '생활', '관리', '운영', '공원', '국유']

    article :  '대구·경북첨단의료산업진흥재단 의약생산센터는 항암주사제 무균충전 시설을 갖추고 있다.', '대구·경북첨단의료 산업진흥재단(이하 대구첨복재단) 의약생산센터는 주세제 특수제제인 세포독성항암주사제제 품질관리기준(GMP)을 인증받았다고 31일 밝혔다.', '의약생산센터는 2016년 완제의약품, 2017년 원료 의약품에 대해 GMP 적합 승인을 받았다.', '올해는 내용고형제 와 원료의약품의 GMP 적합 여부 갱신 확인을 지난 4월 받은 데 이어 주사제 특수제제 생산시설 GMP 적합 여부 평가 승인을 지난 19일 받았다.', '세포독성항암제제는 약사법 시행규칙에서 정한 바에 따라 전용의 분리된 생산시설에서 생산돼야 한다.', '이번 에 GMP 인증을 받은 주사제 생산시설은 세포독성 항암제제 생산을 위한 전용시설로 무균충전용 아이솔레이터(외부와의 접촉을 봉쇄하기 위한 장비)를 포함한 첨단 의약품 생산 및 품질관리 장비를 갖추고 있다.', '이번 GMP 인증을 통해 의약생산센터는 국내 에서 연구 개발되고 있는 세포독성 항암의약품을 시험생산 할 수 있게 됐다.', '세포독성 항암제를 이용한 항체결합의약품의 생 산 지원을 폭넓게 수행할 수 있게 된 것이다.', '국내에서는 세포독성 항암제를 생산할 수 있는 GMP 시설에 제한이 있어 중국 등 외국에 의뢰를 검토하는 실정이다.', '김훈주 의약생산센터장은 “특수제제의약품 생산시설 GMP 인증 완료를 통해 항체결합 의 약품 등 세포독성 의약품 생산시설을 이용하고자 하는 제약기업 및 연구기관 등을 지원할 수 있게 됐다”고 설명했다.'

    summarize_0 ', ' 세포 독성 항암제제는 약사법 시행규칙에서 정한 바에 따라 전용의 분리된 생산시설에서 생산돼야 한다.

    summarize_1 ', ' 이번에 GMP 인증을 받은 주사제 생산시설은 세포 독성 항암제제 생산을 위한 전용시설로 무균 충전용 아이 솔 레이터( 외부와의 접촉을 봉쇄하기 위한 장비 )를 포함한 첨단 의약품 생산 및 품질관리 장비를 갖추고 있다.

    summarize_2 ', ' 국내에서는 세포 독성 항암제를 생산할 수 있는 GMP 시설에 제한이 있어 중국 등 외국에 의뢰를 검토하는 실정이다.

    keywords :  ['생산', '독성', '세포', '시설', '인증', '특수', '센터', '의약', '의약품', '첨단']



todo : 다른요약방법 찾기