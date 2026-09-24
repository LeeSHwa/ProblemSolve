# [level 2] 입양 시각 구하기(1) - 59412 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59412) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2026년 09월 24일 22:04:36

### 문제 설명

<p><code>ANIMAL_OUTS</code> 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. <code>ANIMAL_OUTS</code> 테이블 구조는 다음과 같으며, <code>ANIMAL_ID</code>, <code>ANIMAL_TYPE</code>, <code>DATETIME</code>, <code>NAME</code>, <code>SEX_UPON_OUTCOME</code>는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ANIMAL_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>ANIMAL_TYPE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DATETIME</td>
<td>DATETIME</td>
<td>FALSE</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>SEX_UPON_OUTCOME</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>보호소에서는 <web-highlight class="webhighlights-highlight" data-highlight-id="cf8038ed-23a6-4e4c-a8c9-e86383def6a8" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab51ee2bc1ad94e9575ca2c" media-type="blockquote" style="background-color: rgb(248, 252, 70); cursor: pointer; color: rgb(0, 0, 0);">몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.</web-highlight> <web-highlight class="webhighlights-highlight" data-highlight-id="acbdcf3f-f070-484f-857e-f751a810b2f2" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab51ee9bc1ad94e9575ca2f" media-type="blockquote" style="background-color: rgb(255, 173, 42); cursor: pointer; color: rgb(0, 0, 0);">09:00부터 19:59까지</web-highlight>, <web-highlight class="webhighlights-highlight" data-highlight-id="b365ae7f-a697-477d-8d9a-5911d7c30ee6" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab51ef6bc1ad94e9575ca30" media-type="blockquote" style="background-color: rgb(255, 173, 42); cursor: pointer; color: rgb(0, 0, 0);">각 시간대별로 입양이 몇 건이나 발생했는지 조회</web-highlight>하는 SQL문을 작성해주세요. 이때 결과는 <web-highlight class="webhighlights-highlight" data-highlight-id="df7207f1-94fa-4fb3-b8b0-7c185fc7179e" data-highlight-split-type="both" data-highlight-id-extra="" markid="6ab51efbbc1ad94e9575ca31" media-type="blockquote" style="background-color: rgb(248, 252, 70); color: rgb(0, 0, 0); cursor: pointer;">시간대 순으로 정렬</web-highlight>해야 합니다.</p>

<h5>예시</h5>

<p>SQL문을 실행하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>HOUR</th>
<th>COUNT</th>
</tr>
</thead>
        <tbody><tr>
<td>9</td>
<td>1</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
</tr>
<tr>
<td>11</td>
<td>13</td>
</tr>
<tr>
<td>12</td>
<td>10</td>
</tr>
<tr>
<td>13</td>
<td>14</td>
</tr>
<tr>
<td>14</td>
<td>9</td>
</tr>
<tr>
<td>15</td>
<td>7</td>
</tr>
<tr>
<td>16</td>
<td>10</td>
</tr>
<tr>
<td>17</td>
<td>12</td>
</tr>
<tr>
<td>18</td>
<td>16</td>
</tr>
<tr>
<td>19</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges