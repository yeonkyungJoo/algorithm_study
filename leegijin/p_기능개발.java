package leegijin;

import java.util.LinkedList;
import java.util.Queue;

public class p_기능개발 {
    public static void main(String[] args) {
        int [] progresses = {93, 30, 55};
        int [] speeds = {1, 30, 5};
        int [] answers =solution(progresses,speeds);
        System.out.println(answers[0]+" , "+answers[1]);
    }
    public static int[] solution(int[] progresses, int[] speeds) {
        int[] pro = progresses;
        Queue<Integer> result = new LinkedList<>();
        int index = 0, count = 0;

        while (index < pro.length) {
            for (int i = 0; i < pro.length; i++) {
                pro[i] += speeds[i];
            }

            if (pro[index] >= 100) {
                while(index < pro.length && pro[index] >= 100) {
                    count++;
                    index++;
                }

                result.offer(count);
                count = 0;
            }
        }

        int[] answer = new int[result.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = result.poll();
        return answer;
    }
}
