import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class MyHashTable<K, V> {
    
    private HashEntry[] hashTable;
    private int tableSize;
   
    
    public MyHashTable(int capacity) { // 32768 2^15 entries
        hashTable = new HashEntry[capacity];
        tableSize = capacity;   
    }
    
    public HashEntry[] getTable() {
        return hashTable;
    }
    
    //Puts the key and value designated into MyHashTable
    public void put(K searchKey, V newValue) { 
        HashEntry<String, String> entry = new HashEntry(searchKey, newValue);
        K key = (K) entry.getKey();
        V code = (V) entry.getValue();
        
        int hashCode = hash(key);
        
        int probing = hashCode;
       
        boolean updateSuccess = false;
       
        while((hashTable[probing] != null) && !updateSuccess) {
            probes++;
            if(hashTable[probing].getKey().equals(searchKey)) {
                updateSuccess = true;
            } else {
                probing++;
                if(probing == tableSize) { // if last indexOf hashtable, wrap around and probe from beginning of hashtable
                    probing = 0;
                }
            }
        }

        initialProbes.add(probes);
        hashTable[probing] = entry; // if null bucket, then add entry         
    }
    
   
    public V get(K searchKey) {
        int hashIndex = hash(searchKey);

        if(hashTable[hashIndex].getKey().equals(searchKey)) {
            return (V) hashTable[hashIndex].getValue();
        } else {
            while(hashTable[hashIndex] != null && !hashTable[hashIndex].getKey().equals(searchKey)) {
                hashIndex++;
                if(hashIndex == tableSize) {
                    hashIndex = 0;
                }
            }
        }
        return (V) hashTable[hashIndex].getValue();
    }
    
    public boolean containsKey(K searchKey) {
        int hashIndex = hash(searchKey);
        while(hashIndex < hashTable.length && hashTable[hashIndex] != null) {
           if(hashTable[hashIndex].getKey().equals(searchKey)) {
               return true;
           }
           hashIndex++;
        }
        return false;
    }
    
    private int hash(K key) {
        return Math.abs(key.hashCode()) % tableSize;
    }
    
    public static class HashEntry<K, V> {
        
        private K word;
        
        private V value;
        
        public HashEntry(K searchKey, V newValue) {
            
            word = (K) searchKey;
            value = (V) newValue;
        }
        
        // Returns the HashEntry's Key
        public K getKey() {
            return (K) word;
        }
        
        // Returns the HashEntry's Value
        public V getValue() {
            return (V) value;
        }
    }

}
