package leegijin;

import java.util.*;

public class p_메뉴리뉴얼 {
    static char[] comb;
    static HashMap<String, Integer> map = new HashMap<>();
    public static void main(String[] args) {
        String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
        int [] course ={2,3,4};
        String[] tmp = solution(orders,course);
        for(String t : tmp){
            System.out.println("t = " + t);
        }
    }
    static void combination(char[] menu, int n1, int n2, int r){
            if(n1 == r) {
                String output = String.valueOf(comb);
                map.put(output, map.getOrDefault(output, 0) + 1);
                return;
            }
            for(int i = n2 ; i < menu.length ; i ++){
                comb[n1] = menu[i];
                combination(menu, n1 + 1, i + 1, r);

            }
        }
        public static String[] solution(String[] orders, int[] course) {
            String[] answer = {};

            for(int i : course){
                for(String menu : orders){
                    char[] t_menu = menu.toCharArray();
                    comb = new char[i];
                    Arrays.sort(t_menu);
                    combination(t_menu, 0, 0, i);
                }
            }
            ArrayList<String> ans = new ArrayList<>();
            for(int i : course){
                String get = "";
                int max = 0;
                for(String key : map.keySet()) {
                    if(key.length() == i && map.get(key) > 1){
                        max = Math.max(max, map.get(key));
                    }
                }
                for(String key : map.keySet()){
                    if(key.length() == i && map.get(key) == max) ans.add(key);
                }
            }
            Collections.sort(ans);
            answer = new String[ans.size()];
            int i = 0;
            for(String menu : ans) answer[i ++] = menu;
            return answer;
        }
    }