class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        set<string> result; //repeated
        set<string> sequences; //seen
        int i = 0;
        while ((i + 10) <= s.size()) {
            //get 10 chars from string
            string substr = s.substr(i, 10);
            //find returns the end if substr is not present
            if (sequences.find(substr) == sequences.end()) {
                //haven't seen, add to sequences
                sequences.insert(substr);
            } else {
                //have seen, add to result
                result.insert(substr);
            }
            i++;
        }
        return vector<string>(result.begin(), result.end());
    }
};
