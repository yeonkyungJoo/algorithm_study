package leegijin;

import java.util.ArrayList;

public class p_스킬트리 {
    public static void main(String[] args) {
        String skill ="CBD";
        String []skill_trees = {"BACDE", "CBADF", "AECB", "BDA"};
        System.out.println(solution(skill,skill_trees));
    }
    public static int solution(String skill, String[] skill_trees) {
        int answer = 0;
        for(int z=0; z< skill_trees.length ; z++){
            ArrayList<Integer> a = new ArrayList<>();
            for(int j=0; j< skill.length(); j++){
                int tmp =skill_trees[z].indexOf(skill.charAt(j));
                a.add(tmp);
            }
            int flag =1;
            for(int i=0; i<a.size()-1; i++) {
                if(a.get(i)==-1 && a.get(i+1)!=-1)  //이전스킬을 못배웠는데 다음스킬트리를 배운경우
                {
                    System.out.println("=====이전스킬을 못배웠는데 다음스킬트리를 배운경우======="+skill_trees[z]);
                    flag=0;
                    break;
                }
                else if(a.get(i)<=a.get(i+1) || a.get(i+1)==-1) { //잘 순서대로 잘 배운경우  //
                    continue;
                }
                else {   // 스킬트리를 다 배웠지만 순서대로 배우지 못한경우
                    System.out.println("=====스킬트리를 다 배웠지만 순서대로 배우지 못한경우======="+skill_trees[z]);
                    flag=0;
                    break;
                }
            }
            if(flag==1)
                answer++;
        }
        return answer;
    }
}
