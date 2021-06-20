import java.util.*;

public class p_숫자게임 {

    public static final int INF = -1;

    public static void main(String[] args) {
        int [] A = {5,1,3,7};
        int [] B = {2,2,6,8};
        System.out.println(solution(A,B));
    }
    public static int solution(int[] A, int[] B) {
        int answer = 0;

        // sort 
        Arrays.sort(A);
        Arrays.sort(B);

        // A를 이길 수 있는 B 찾기 (끝에서부터)
        int i_b = A.length-1;
        for(int i_a=A.length-1; i_a >=0; i_a--){
            // 이기는 패
            if (B[i_b] > A[i_a]){
                answer++;
                i_b--;
            }
        }

        return answer;
    }
}