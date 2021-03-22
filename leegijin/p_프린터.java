package leegijin;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class p_프린터 {
    public static void main(String[] args) {
        int [] priorities ={2, 1, 3, 2};
        int location = 2;
        System.out.println(solution(priorities,location));
    }
    public static int solution(int[] priorities, int location) {
        int answer = 0;
        ArrayList<Integer> prior = new ArrayList<>();
        for(int i =0 ; i<priorities.length ; i++){  //우선순위 저장
            prior.add(priorities[i]);
        }
        Queue<Integer> queue = new LinkedList<>();
        for(int i =0; i<priorities.length ; i++){   // location을 저장하는 큐
            queue.add(i);
        }

        int cnt =1;
        while(!queue.isEmpty()) {
            boolean isMax = true;  // prior안에 최대값인지 확인하는 플래그
            for (int i = 1; i < prior.size(); i++) {
                if (prior.get(0) < prior.get(i)) {
                    int tmp = prior.remove(0); //아니면 뺏다가 다시 add
                    prior.add(tmp);
                    int qtmp = queue.poll();
                    queue.add(qtmp);
                    isMax = false;
                }
            }
            if (isMax) {
                prior.remove(0);
                int temp = queue.poll();
                if (temp == location) {
                    answer = cnt;
                    return answer;
                }
                cnt++;
            } else
                continue;
        }
        return answer;
    }
}
