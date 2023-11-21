
/*
위와 같이 서로 다른 연산 순서의 계산 결과는 [-15, -5, -5, 1, 1]이 되며, 이중 최댓값은 1입니다.
문자열 형태의 숫자와, 더하기 기호("+"), 뺄셈 기호("-")가 들어있는 배열 arr가 매개변수로 주어질 때,
서로 다른 연산순서의 계산 결과 중 최댓값을 return 하도록 solution 함수를 완성해 주세요.

https://school.programmers.co.kr/learn/courses/30/lessons/1843
*/


function solution (arr) {
  const operandsCount = Math.ceil(arr.length / 2);
  const max_dp = new Array(operandsCount).fill().map(_ => new Array(operandsCount).fill(-Infinity));
  const min_dp = new Array(operandsCount).fill().map(_ => new Array(operandsCount).fill(Infinity));
  
  for(let i = 0; i < operandsCount; i++) {
    max_dp[i][i] = +arr[i*2];
    min_dp[i][i] = +arr[i*2];
  }
  
  for(let cnt = 1; cnt < operandsCount; cnt++) {
    for(let i = 0; i < operandsCount - cnt; i++) {
      const j = i + cnt;
      for(let k = i; k < j; k++) {
        if (arr[k*2+1] === '+') {
          max_dp[i][j] = Math.max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j]);
          min_dp[i][j] = Math.min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j]);
        } else {
          max_dp[i][j] = Math.max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j]);
          min_dp[i][j] = Math.min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j]);
        }
      }
    }
  }
  
  return max_dp[0][operandsCount-1];
}