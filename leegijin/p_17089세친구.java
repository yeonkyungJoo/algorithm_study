package leegijin;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class p_17089세친구 {
    static int n;
    static boolean map[][];
    static int min = Integer.MAX_VALUE;
    static int temp = 0;
    static int fcnt[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s;
        s = new StringTokenizer(br.readLine());
        n = Integer.parseInt(s.nextToken());
        int m = Integer.parseInt(s.nextToken());
        map = new boolean[n + 1][n + 1];
        fcnt = new int[n + 1];
        for (int i = 0; i < m; i++) {
            s = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(s.nextToken());
            int b = Integer.parseInt(s.nextToken());
            map[a][b] = true;
            map[b][a] = true;
            fcnt[a]++;
            fcnt[b]++;
        }
        int result = -1;
        for (int a = 1; a <= n; a++) {
            for (int b = a+1; b <= n; b++) {
                if (map[a][b]) {
                    for (int c = b+1; c <= n; c++) {
                        if (map[a][c] && map[b][c]) {
                            int sum = fcnt[a] + fcnt[b] + fcnt[c] - 6;
                            if (result == -1 || result > sum)
                                result = sum;
                        }
                    }
                }
            }
        }
        System.out.println(result);
    }
}
