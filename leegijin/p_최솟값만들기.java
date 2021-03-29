package leegijin;

import java.util.Arrays;

public class p_최솟값만들기 {
    public static void main(String[] args) {
        int [] arr ={1, 4, 2};
        int [] arr1 ={5, 4, 4};
        System.out.println(solution(arr,arr1));
    }
    public static int solution(int []A, int []B)
    {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        for(int i =0 ; i< A.length ; i++) {
            answer=answer+A[i]*B[A.length-i-1];
        }
        return answer;
    }
}
