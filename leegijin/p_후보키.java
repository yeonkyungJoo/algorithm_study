package leegijin;

        import java.util.ArrayList;
        import java.util.HashSet;
        import java.util.List;
        import java.util.Set;

public class p_후보키 {
    public static void main(String[] args) {
        String[][] relation = {{"100","ryan","music","2"},{"200","apeach","math","2"},{"300","tube","computer","3"},{"400","con","computer","4"}
                ,{"500","muzi","music","3"},{"600","apeach","music","2"}};
        System.out.println(solution(relation));
    }
    static Set<HashSet<Integer>> candidiateKey = new HashSet<HashSet<Integer>>();
    static int count = 0;

    public static void backtracking(String[][] relation, int depth, List<Integer> list, int n, int k, int data[]) {

        if (list.size() == k) {

            // 최소성검사
            for (HashSet<Integer> temp : candidiateKey) {
                int size = temp.size();
                int m = 0;
                for (int i = 0; i < list.size(); i++) {
                    if (temp.contains(list.get(i))) {
                        m++;
                    }
                }
                if(size == m) {
                    return;
                }
            }

            Set<String> set = new HashSet<String>();
            for (int j = 0; j < relation.length; j++) {

                StringBuilder builder = new StringBuilder();
                for (int i = 0; i < list.size(); i++) {
                    builder.append(relation[j][list.get(i)]);
                }
                set.add(builder.toString());
            }
            // 후보키만족
            if (set.size() == relation.length) {
                HashSet<Integer> temp = new HashSet<Integer>();
                for (int i = 0; i < list.size(); i++) {
                    temp.add(list.get(i));
                }
                candidiateKey.add(temp);
                count++;
            }
            return;
        }

        if (depth == n) {
            return;
        }

        list.add(data[depth]);

        backtracking(relation, depth + 1, list, n, k, data);

        list.remove(list.size() - 1);
        backtracking(relation, depth + 1, list, n, k, data);

    }

    public static int solution(String[][] relation) {

        int answer = 0;

        // 데이터
        int row = relation.length;
        // col이 키
        int col = relation[0].length;
        int data[] = new int[col];
        for (int i = 0; i < col; i++) {
            data[i] = i;
        }
        List<Integer> list = new ArrayList<Integer>();
        for (int i = 1; i <= col; i++) {
            backtracking(relation, 0, list, col, i, data);
        }
        answer = count;
        return answer;

    }

}
