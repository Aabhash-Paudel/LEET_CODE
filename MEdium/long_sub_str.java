import java.util.HashMap;

public class long_sub_str {
    public static int findMaxLength(String s) {
        String vowels = "aeiou";
        int state = 0;
        HashMap<Integer, Integer> firstOccurrence = new HashMap<>();
        firstOccurrence.put(0, -1);
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (vowels.indexOf(ch) != -1) {
                state ^= 1 << vowels.indexOf(ch);
            }

            if (firstOccurrence.containsKey(state)) {
                maxLength = Math.max(maxLength, i - firstOccurrence.get(state));
            } else {
                firstOccurrence.put(state, i);
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        String s = "your_input_string_here";  // Replace with your input string
        System.out.println(findMaxLength(s));
    }
}
