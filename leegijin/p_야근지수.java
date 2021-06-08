import java.util.Arrays;

public class p_야근지수 {
    public static void main(String[] args) {
        int[] works = {4,3,3};
        int n=4;
        System.out.println(solution(n,works));
    }
    public static long solution(int n, int[] works) {
        long answer = 0;
        int max = 0;
        int index = 0;

        Arrays.sort(works);

        while (n > 0) {
            index = works.length - 1;
            max = works[works.length - 1];
            for (int i = works.length - 2; i > -1; i--) {
                if (max < works[i]) {
                    max = works[i];
                    index = i;
                    break;
                }
            }
            works[index]--;
            n--;
        }

        for (int i : works) {
            if(i > 0)
                answer += i * i;
        }
        return answer;
    }
}
