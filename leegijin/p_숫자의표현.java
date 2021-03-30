package leegijin;

public class p_숫자의표현 {
    public static void main(String[] args) {
            int n =15;
        System.out.println(solution(n));
    }
    public static int solution(int n) {
        int answer = 0;

        for (int i = 1; i <= n; i++){
            if (n % i == 0) {
                if (i % 2 == 1)
                    answer++;
            }
        }


        return answer;
    }
}
