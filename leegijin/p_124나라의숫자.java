public class p_124나라의숫자 {
    public static void main(String[] args) {
        System.out.println(solution(10));
    }
    public static String solution(int n) {
        String[] numbers = {"4", "1", "2"};
        String answer = "";

        int num = n;

        while(num > 0){
            int remainder = num % 3;  // 3진수랑 비슷하지만 나머지가 0일때 달라집니다.
            num /= 3;

            if(remainder == 0) num--;

            answer = numbers[remainder] + answer;
        }

        return answer;
    }
}
