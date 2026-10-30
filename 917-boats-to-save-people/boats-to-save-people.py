class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Array ko ascending order (chhote se bada) me sort karna hai
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        #Two pointers ka use karke pairs process karna hai 
        while left <= right:
            #Agar lightest (sabse halka) aur heaviest (sabse bhari) insaan ek hi boat me fit ho sakte hai
            if left != right and (people[right] + people[left] <= limit):
                left += 1 # Lightest insaan boat mein baith gaya, toh left pointer aage badhao

            right -= 1 # Heaviest insaan ko toh boat milegi hi (chahe akela baithe ya pair ke sath)
            boats += 1
        return boats




        