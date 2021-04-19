package leegijin;

import java.util.ArrayList;

public class p_짝지어제거하기 {
    public static void main(String[] args) {
        String s ="baabaa";
        System.out.println(solution(s));
    }
    public static int solution(String s)
    {
        int answer = 0;
        ArrayList<Character> a = new ArrayList<>();
        for(int i =0; i<s.length() ; i++) {
            if(a.size()!=0&&s.charAt(i)==a.get(a.size()-1))
                a.remove(a.size()-1);
            else
                a.add(s.charAt(i));
        }
        if(a.size()==0)
            answer = 1;
        else
            answer =0;
        return answer;
    }
}
