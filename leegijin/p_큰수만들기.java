package leegijin;

public class p_큰수만들기 {
    public static void main(String[] args) {
        String number ="578578578123451234599797895";
        int k =10;
        System.out.println(solution(number,k));
    }
    public static String solution(String number, int k) {
        StringBuilder answer = new StringBuilder();
        char max;
        int idx = 0;
        if(number.charAt(0)=='0')
            return "0";
        for(int i = 0; i<number.length()-k; i++) {
            max = '0';
            for(int j = idx; j<=k+i; j++) {
                if(max < number.charAt(j)) {
                    max = number.charAt(j);
                    idx = j+1;
                }
            }
            answer.append(max);
        }
        return answer.toString();
    }
}
