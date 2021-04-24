package leegijin;

import java.util.*;
import java.io.*;

public class p_1253좋다 {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int arr[] = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] =Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            int left = 0, right = N - 1;
            int target = arr[i];
            System.out.println("arr[i] = " + arr[i]);
            while (left < right) {
                int cal = arr[left] + arr[right];
                if (cal < target) {
                    left++;
                } else if (cal > target) {
                    right--;
                } else {
                    if (i != left && i != right) {
                        System.out.println("left = " + left);
                        System.out.println("right = " + right);
                        cnt++;
                        break;
                    }
                    if (left == i)
                        left++;
                    if (right == i)
                        right--;
                }
            }
        }

        System.out.println(cnt);



    }
}