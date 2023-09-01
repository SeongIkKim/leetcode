class Solution {
    public int compress(char[] chars) {
        int i = 0; // letter checking pointer
        int wp = 0; // writing pointer
        while (i < chars.length) {
            int groupLength = 1;
            while (i + groupLength < chars.length && chars[i + groupLength] == chars[i]){
                groupLength++;
            }
            chars[wp++] = chars[i];
            if (groupLength > 1) {
                for (char c : Integer.toString(groupLength).toCharArray()) {
                    chars[wp++] = c;
                }
            }
            i += groupLength; // now check next letter group
        }
        return wp; // last writing index + 1(res++) == compressed length
    }  
}