# [level 2] 가격대 별 상품 개수 구하기 - 131530 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131530) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2026년 09월 24일 22:39:05

### 문제 설명

<p>다음은 어느 의류 쇼핑몰에서 판매중인 상품들의 정보를 담은 <code>PRODUCT</code> 테이블입니다. <code>PRODUCT</code> 테이블은 아래와 같은 구조로 되어있으며, <code>PRODUCT_ID</code>, <code>PRODUCT_CODE</code>, <code>PRICE</code>는 각각 상품 ID, 상품코드, 판매가를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>PRODUCT_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRODUCT_CODE</td>
<td>VARCHAR(8)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRICE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>상품 별로 중복되지 않는 8자리 상품코드 값을 가지며 앞 2자리는 카테고리 코드를 나타냅니다.</p>

<hr>

<h5>문제</h5>

<p><code>PRODUCT</code> 테이블에서 <web-highlight class="webhighlights-highlight" data-highlight-id="fa542d3a-d9e1-49a7-9e41-d111abb05434" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab522e163ac0c1a1156aae1" media-type="blockquote" style="background-color: rgb(248, 252, 70); color: rgb(0, 0, 0); cursor: pointer;">만원 단위의 가격대 별</web-highlight>로 <web-highlight class="webhighlights-highlight" data-highlight-id="c4eaa800-8cb4-481f-88f4-ab9cdbe21100" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab522e663ac0c1a1156aae2" media-type="blockquote" style="background-color: rgb(255, 173, 42); color: rgb(0, 0, 0); cursor: pointer;">상품 개수를 출력</web-highlight>하는 SQL 문을 작성해주세요. 이때 컬럼명은 각각 <web-highlight class="webhighlights-highlight" data-highlight-id="75d6e190-ef51-4dab-9d19-8597a35bc850" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab5231263ac0c1a1156aae3" media-type="blockquote" style="background-color: rgb(146, 255, 170); cursor: pointer; color: rgb(0, 0, 0);">컬럼명은 PRICE_GROUP</web-highlight>, <web-highlight class="webhighlights-highlight" data-highlight-id="b2a457d6-5048-46bb-ae96-ebe27c9048b8" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab5232063ac0c1a1156aae4" media-type="blockquote" style="background-color: rgb(146, 255, 170); color: rgb(0, 0, 0); cursor: pointer;">PRODUCTS</web-highlight>로 지정해주시고 <web-highlight class="webhighlights-highlight" data-highlight-id="de1b16d7-66d7-4cf4-a153-790bde7a26f4" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab5233263ac0c1a1156aae6" media-type="blockquote" style="background-color: rgb(251, 131, 179); color: rgb(0, 0, 0); cursor: pointer;">가</web-highlight><web-highlight class="webhighlights-highlight" data-highlight-id="af67285a-8920-45a1-a10e-a1ca3f66a79e" data-highlight-split-type="tail" data-highlight-id-extra="" markid="6ab5232f63ac0c1a1156aae5" media-type="blockquote" style="background-color: rgb(251, 131, 179); cursor: pointer; color: rgb(0, 0, 0);">격대 정보는 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000</web-highlight>)으로 표시해주세요. <web-highlight class="webhighlights-highlight" data-highlight-id="ec57b29e-aaed-4e77-b033-7ca4a5cc3ced" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab5233d63ac0c1a1156aae7" media-type="blockquote" style="background-color: rgb(146, 255, 170); color: rgb(0, 0, 0); cursor: pointer;">결과는 가격대를 기준으로 오름차순 정렬</web-highlight>해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>PRODUCT</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>PRODUCT_ID</th>
<th>PRODUCT_CODE</th>
<th>PRICE</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>A1000011</td>
<td>10000</td>
</tr>
<tr>
<td>2</td>
<td>A1000045</td>
<td>9000</td>
</tr>
<tr>
<td>3</td>
<td>C3000002</td>
<td>22000</td>
</tr>
<tr>
<td>4</td>
<td>C3000006</td>
<td>15000</td>
</tr>
<tr>
<td>5</td>
<td>C3000010</td>
<td>30000</td>
</tr>
<tr>
<td>6</td>
<td>K1000023</td>
<td>17000</td>
</tr>
</tbody>
      </table>
<p>만원 단위의 가격대 별로 상품을 나누면</p>

<ul>
<li>가격대가 0원 ~ 1만원 미만인 상품은 <code>PRODUCT_ID</code> 가 2인 상품 1개,</li>
<li>가격대가 1만원 이상 ~ 2만원 미만인 상품들은 <code>PRODUCT_ID</code> 가 1, 4, 6인 상품 3개,</li>
<li>가격대가 2만원 이상 ~ 3만원 미만인 상품은 <code>PRODUCT_ID</code> 가 3인 상품 1개,</li>
<li>가격대가 3만원 이상 ~ 4만원 미만인 상품은 <code>PRODUCT_ID</code> 가 5인 상품 1개,</li>
</ul>

<p>에 각각 해당하므로 다음과 같이 결과가 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>PRICE_GROUP</th>
<th>PRODUCTS</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>10000</td>
<td>3</td>
</tr>
<tr>
<td>20000</td>
<td>1</td>
</tr>
<tr>
<td>30000</td>
<td>1</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges