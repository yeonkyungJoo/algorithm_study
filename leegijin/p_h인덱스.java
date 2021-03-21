package leegijin;

import java.util.Arrays;

public class p_h인덱스 {
    public static void main(String[] args) {
        int citations[] = {5,5,5,5,5};
        System.out.println(solution(citations));
    }
    public static int solution(int[] citations) {
        int answer = 0;

        Arrays.sort(citations);
        for (int i = 0; i < citations.length; i++) {
            int h = citations.length - i;

            if (citations[i] >= h) {
                answer = h;
                break;
            }
        }
        return answer;
    }
}
