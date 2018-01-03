---
layout: post
title: "번역 풀리퀘를 처음으로 넣어보았다"
date: 2017-01-22 02:49:00 +0900
categories: Tech
tags: blog
author: suckzo_o
---

# 첫 Pull Request 이야기, 그리고 번역에서의 용어 표기에 관하여

## 1.

주된 이슈는 정형화된 텀을 번역할 때 어떻게 번역할 것인지에 관한 것입니다. 특히, 제가 지금 건드리는 이슈는 List comprehension라는 용어를 어떻게 표현할까에 관한 문제입니다. 원래는 "리스트 해석"이라고 표현되어 있었습니다.(이 경우, 번역된 자료가 몇 개 존재한다고 합니다.) 저는 이게 굉장히 어색하다고 생각했고, 원래 용어를 그대로 두어 살렸으면 좋겠다는 생각을 했습니다.

## 2.

가독성을 깊게 고민하며 하루종일 [성북동 휘스커](https://twitter.com/cafe_whisker) (마카롱이 맛있습니다.) 에서 번역 개선 작업을 했습니다.
일단 저는 원문 그대로가 제일 낫다고 생각했고, [소소한 설문조사](https://twitter.com/suckzo_o/status/822365846357954564) 에서도 주로 동의한다는 의견이 나와서
"List comprehension"으로 대체하여 [PR](https://github.com/doomspork/elixir-school/pull/935)을 쐈습니다. 그 결과, 두 가지 피드백이 왔습니다.

- 최소한의 번역이라도 해야 한글 사용자들이 용어의 의미를 _그나마_ 잘 추론할 수 있다. 더불어, `해석`이라는 단어로 해석된 자료가 어느정도 있다.
- "리스트 컴프리헨션"이라고 음차를 써서 표현하는 것이 조금 더 나아보인다.

## 3.

List comprehension이 뭔가를 먼저 생각해봤습니다.

```elixir
iex> list = [1, 2, 3, 4, 5]
iex> for x <- list, do: x*x
[1, 4, 9, 16, 25]
```

위의 예제와 같이, 어떤 enumerable한 collection을 iterate하면서 return value를 통해 새로운 collection을 만드는 것입니다.

```elixir
import Integer
iex> for x <- 1..100,
...>   is_even(x),
...>   rem(x, 3) == 0, do: x
[6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
```

이런 방식으로 필터를 이용하여 조건제시법같이 집합을 만들 수도 있습니다. 자세한 설명은 [여기](https://elixirschool.com/lessons/basics/comprehensions/) ([한글 번역](https://elixirschool.com/ko/lessons/basics/comprehensions/)) 에서 보실 수 있습니다.

## 4.

- 번역한 뒤에도 텍스트를 통해 직관적으로 의미를 전달할 수 있어야 합니다.
- 번역된 용어가 일반적으로 잘 받아들여지며 많은 사용자들이 써야합니다.

저는 위의 두 가지를 모두 만족해야 좋은 번역이라고 생각합니다. 위의 두 가지를 정확하게 만족하는 좋은 예시는 `타입 추론`이라고 생각합니다.
사전적 의미를 통해 그대로 번역해도, 값을 통해 변수의 타입을 추측한다는 개념이 매우 자연스럽게 녹아있습니다. 더불어 용어 자체가 널리 사용되고 있기도 합니다.

이런 철학을 갖고 `해석`이라는 챕터를 봤을 때, 저는 전혀 좋은 단어 선정이 아니라고 생각했습니다.
이런 해석이 많은 사람들에게 받아들여져서 사용되었다고 해도,
Comprehension이 리스트를 `해석한다`고 생각되지는 않는 개념이었습니다.

(논외로 어제 받았던 의견 중 `syntactic sugar`를 `꿀문법`으로 번역한다는 사례를 보았습니다)

## 5.

1번 피드백에 대해서 반론하기 위하여 몇 가지를 찾아보며 의견을 제시했습니다.

### 5-1. 해석 -> comprehension으로 이어지는가?

해석을 한영사전에 찾아봤습니다.

![한영사전](/assets/images/170122/KE_dict_query.png)

`interpret`, `read` 등의 단어만 나올 뿐, comprehension이라는 단어를 찾아볼 수 없었습니다.
만약 이 개념을 모르는 사람이 번역본을 봤을 때 구글링 키워드가 `List interpretation`과 같이 변할 수 있겠다는 생각이 우선적으로 들었습니다.
물론 키워드 자체가 틀렸기에, 저 키워드로 구글링하면 관련된 포스트는 찾기 어렵습니다.
좋은 워딩 선정이 힘들어서 `해석`이라는 단어를 선택한 점은 어느정도 이해하지만, 잘못된 방향으로 해석하고 있다는 확신이 들었습니다.

### 5-2. `리스트 해석`이 일반적으로 사용되는 용어인가?

시크릿 탭을 이용하여 `리스트 해석`을 찾아보았습니다.

![리스트 해석](/assets/images/170122/list_haeseok.png)

연관된 주제가 1순위로 랭크되어있지 않을 뿐더러, 검색 결과 1페이지의 대부분이 관련이 없는 내용이었습니다.

`리스트 컴프리헨션`도 찾아보았습니다.

![리스트 컴프리헨션](/assets/images/170122/list_comprehension.png)

바로 원하던 결과를 얻었으며, 검색 결과 1페이지 모두 연관된 내용이었습니다.
이 결과를 대조하며 얻은 두 가지 결론은 다음과 같습니다.

- `리스트 해석`으로 번역된 자료가 일부 있음에도 불구하고, 사람들이 많이 사용하지 않는다.
- 이 개념은 `리스트 컴프리헨션`, 내지는 `List comprehension`이라는 키워드로 이미 넘어갔다.

## 6.

2번 피드백도 동의하기는 힘들었습니다. 우선 당장 외래어 표기법을 헷갈리는 사람이 너무 많습니다.
대표적인 예시로, sh-로 시작하는 모든 단어를 들 수 있습니다. 그 중, 개발자에겐 친숙할 `shell`이라는 단어를 생각해봅시다.
[외래어 표기법](https://www.korean.go.kr/front/page/pageView.do?page_id=P000104&mn_id=97) 제 3장 3항의 2에 따른 올바른 표기법은 `셸`이지만
많은 사람들이 `쉘`이라고 표기합니다.
심지어 제가 소속된 동아리 스팍스에서도 여전히 `쉘 스크립트`와 같은 표기를 사용합니다.
물론 이 경우 `쉘 스크립트`라는 표기가 일반적으로 받아들여지는 표기이기는 합니다.
다만, 모든 용어를 생각해봤을 때 사람마다 제각각의 외래어 표기를 할 것이라고 생각했고,
일관되지 않은 용어 사용으로 혼란을 일으킬 수도 있다는 우려는 여전히 있습니다.

## 7. tl;dr

정리하자면, 제가 생각하는 `번역에서의 올바른 용어 사용법`은 다음과 같습니다.

- 번역된 키워드를 사용할 경우 직관적으로 의미 파악이 가능해야 합니다.
- 이 키워드를 사용할 사람들이 일반적으로 사용하는(혹은 일반적으로 사용하는 데에 이견이 없는) 용어를 선정해야 합니다.
- 이외의 키워드는 원안 유지가 좋다고 생각합니다.

## 8.

이런 이유로, 내일 아침 토익 시험에도 불구하고(...) 장문의 의견을 남겼습니다. 기존 번역 개선 분량의 3~4배쯤은 되는 분량이네요(...)
이번에 풀리퀘스트를 하는 데에 특히 시간을 많이 쓴 부분이 몇 가지 있는데,

- 제가 어색한 문장을 쓰지는 않았는지, 실수한 것은 없는지 더블체크하면서 시간을 굉장히 많이 썼습니다.
- 이 번역본을 영어를 모르는 사람, IT 지식이 부족한 사람이 읽었을 때 문장이 자연스러울지 굉장히 고민을 많이 했습니다.
- PR을 영어로 쓰면서 익숙한 단어도 오용하진 않는지, 문법적인 오류는 없는지 더블체크 하면서도 시간을 굉장히 많이 썼습니다.
- 이 글을 읽고 사람들이 설득이 될지 고민하면서 시간을 굉장히 많이 썼습니다.

영어 잘 하고 싶습니다. 여튼 고생해서 넣은 PR인데 잘 협의가 끝나고 온전히 머지가 되었으면 좋겠다는 생각입니다.

## 9.

- 제 PR이 아직 머지되지는 않았습니다! 여전히 개선한 번역에서도 어색한 부분, 내지는 개선의 여지가 있는 부분이 있을 수 있으니 도와주시면 진짜 감사드리겠습니다 (\_ \_)
- 번역 PR이 가장 쉬운 PR이기도 하고, 더불어 공부도 잘 됩니다! 여러분 번역하세요.
- Elixirschool 한국어 번역판 번역 퀄리티 꽤 괜찮습니다! 이 참에 재밌는 elixir를 다같이 배워보시는 건 어떤가요!
- 의견이 갈릴 수 있는 글이라고 생각합니다! 글에 대한 피드백도 언제든지 환영입니다 :)