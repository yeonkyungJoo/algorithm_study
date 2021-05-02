package leegijin;

import java.io.*;
import java.util.*;

public class p_16637괄호추가하기 {
    static int len;
    static int max = -123456789;
    public static void cal(LinkedList<Integer> n, LinkedList<Character> o, int idx) {
        char op = o.remove(idx);
        int num1 = n.remove(idx);
        int num2 = n.remove(idx);
        if(op == '+') {
            n.add(idx, num1 + num2);
        }
        else if(op == '-') {
            n.add(idx, num1 - num2);
        }
        else if(op == '*') {
            n.add(idx, num1 * num2);
        }
    }

    public static void dfs(int x, int flag, LinkedList<Integer> n, LinkedList<Character> o) {
        LinkedList<Integer> nums = new LinkedList<>();
        LinkedList<Character> op = new LinkedList<>();
        nums.addAll(n);
        op.addAll(o);

        if(x > op.size() - 1 || x > len - 1) {
            while(nums.size() > 1) {
                cal(nums, op, 0);
            }
            max = Math.max(nums.get(0), max);
            return;
        }

        if(flag == 1) {
            cal(nums, op, x);
        }
        dfs(x + 1, 1, nums, op);
        dfs(x + 1, 0, nums, op);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        len = n / 2;
        String s = br.readLine();
        LinkedList<Integer> nums = new LinkedList<>();
        LinkedList<Character> op = new LinkedList<>();
        for(int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if(i % 2 == 0) nums.add(c - '0');
            else op.add(c);
        }

        dfs(0, 0, nums, op);
        dfs(0, 1, nums, op);
        System.out.println(max);
    }
}