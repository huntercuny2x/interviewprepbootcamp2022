class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
      
        //26 is alphabet size
        vector<int> hash(26, 0);
        vector<int> phash(26, 0);
      
        //idx 0 has freq of a, idx 1 has freq of b etc
        int window = p.size();
        int len = s.size();
        
        //returns empty vector if s is smaller than p
        if(len < window) {
            return ans;
        }
        //window boundaries
        int left = 0,right = 0;
        while(right < window) {
            phash[p[right] - 'a'] += 1;
            hash[s[right] - 'a'] += 1;
            right++;
        }
        right -=1;
        while(right < len) {
            if(hash == phash) {
                ans.push_back(left);
            }
            right+=1;
            if(right != len) {
                hash[s[right] - 'a'] += 1;
            }
            hash[s[left] - 'a'] -=1 ;
            left += 1;
        }
        return ans;
    }
};
