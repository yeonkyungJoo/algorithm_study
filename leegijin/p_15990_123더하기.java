package leegijin;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class p_15990_123더하기 {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final int MOD = 1000000009;

    public static void main(String[] args) throws Exception {
        int t = Integer.parseInt(br.readLine());

        long[][] dp = new long[100001][4];

        dp[1][1] = 1;
        dp[2][2] = 1;
        dp[3][1] = dp[3][2] = dp[3][3] = 1;

        for (int i = 4; i <= 100000; i++) {
            dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD;
            dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD;
            dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            sb.append((dp[n][1] + dp[n][2] + dp[n][3]) % MOD).append("\n");
        }
        System.out.print(sb);
    }
}