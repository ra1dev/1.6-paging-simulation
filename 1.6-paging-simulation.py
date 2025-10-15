#initialise page table in a dictionary
page_table = { 
	0b00000: 0b01001, #0, 9 
	0b00001: 0b00001, #1, 1 
	0b00010: 0b01110, #2, 14 
	0b00011: 0b01010, #3, 10 
	0b00100: None, #4. page fault 
	0b00101: 0b01101, #5, 13 
	0b00110: 0b01000, #6,8 
	0b00111: 0b01111, #7, 15 
	0b01000: None, #8, page fault 
	0b01001: 0b11110, #9, 30 
	0b01010: 0b10010, #10, 18 
	0b01011: None, #11, page fault 
	0b01100: 0b10101, #12, 21 
	0b01101: 0b11011, #13, 27 
	0b01110: None, #14, page fault 
	0b01111: 0b10110, #15, 22 
	0b10000: 0b11101, #16, 29 
	0b10001: None, #17, page fault 
	0b10010: 0b10011, #18, 19 
	0b10011: 0b11010, #19, 26 
	0b10100: 0b10001, #20, 17 
	0b10101: 0b11001, #21, 25 
	0b10110: None, #22, page fault 
	0b10111: 0b11111, #23, 31 
	0b11000: 0b10100, #24, 20 
	0b11001: 0b00000, #25, 0 
	0b11010: 0b00101, #26, 5 
	0b11011: 0b00100, #27, 4 
	0b11100: None, #28, page fault 
	0b11101: None, #29, page fault 
	0b11110: 0b00011, #30, 3 
	0b11111: 0b00010, #31, 2 
}

#function to map page number to frame number
def map_page_to_frame(page_number):

    #checks if page number is in the page table
    if page_number in page_table:
        frame = page_table[page_number]

        #checks if there is a page fault
        if frame is None:
            return None
        else:
            return frame
        
#function to convert page number and page offset into a virtual memory address
def virtual_memory_address(page_number, page_offset):
    
    #converts binary input to string without 0b prefix
    page_number_str = bin(page_number)[2:].zfill(5)  
    page_offset_str = bin(page_offset)[2:].zfill(8)  

    #concatenate page number and poge offset string
    virtual_memory_str = page_number_str + page_offset_str

    #convert to string to integer
    virtual_memory_int = int(virtual_memory_str,2)

    #return integer as string without 0b prefix
    return virtual_memory_str

def main():
    #ask for user input
    page_number = int(input("Input the 5-bit digits binary format for virtual memory page number: "), 2)
    page_offset = int(input("Input the 8-bit digits binary format for virtual page offset: "), 2)

    #call and print virtual_memory_address function to print virtual memory address
    print("The virtual memory address you keyed in is: " + virtual_memory_address(page_number, page_offset))

    #
    frame_number = map_page_to_frame(page_number)

    if frame_number == None:
        print("There is a page error")

    else: 
        print("The physical memory address to be accessed after paging is: " + virtual_memory_address(frame_number, page_offset))

if __name__ == "__main__":
    main()