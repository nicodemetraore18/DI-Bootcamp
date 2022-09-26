"""Instructions :
Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

The Pagination class will accept 2 parameters:

items (default: []): A list of contents to paginate.
pageSize (default: 10): The amount of items to show in each page.
So for example we could initialize our pagination like this:

alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)


The Pagination class will have a few methods:

getVisibleItems() : returns a list of items visible depending on the pageSize
So for example we could use this method like this:

p.getVisibleItems() 
# ["a", "b", "c", "d"]
You will have to implement various methods to go through the pages such as:
prevPage()
nextPage()
firstPage()
lastPage()
goToPage(pageNum)

Here’s a continuation of the example above using nextPage and lastPage:

alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)

p.getVisibleItems() 
# ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]


Notes

The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).
"""
import numpy as np
class Pagination :
	def __init__(self,items=[],pageSize=10):
		self.items=items
		self.pageSize=pageSize
		self.origin=0
		self.currentPage=1
		self.totalPage=len(self.items)/self.pageSize
		if type(self.totalPage)=="int":
			pass
		elif type(self.totalPage)=="float":
			self.totalPage=int(self.totalPage)+1

	def getVisibleItems(self):
		arr=np.array(self.items)
		newarr=arr[self.origin:(self.origin+self.pageSize)]
		print(newarr)

	def prevPage(self):
		if self.origin==0:
			print("No previous Page this is the first page")
		else:
			self.origin-=10
			self.currentPage-=1
		return self

	def nextPage(self):
		if self.origin+10>len(self.items):
			print("This page is the last")
		else:
			self.origin+=10
			self.currentPage+=1
		return self

	def firstPage(self):
		self.origin=0
		self.currentPage=1
		return self

	def lastPage(self):
		reste=len(self.items)%self.pageSize
		if reste==0:
			self.origin=len(self.items)-self.pageSize
		elif reste>0:
			self.origin=len(self.items)-reste
		self.currentPage=self.totalPage
		return self

	def goToPage(self,pageNum):
		if pageNum>=self.totalPage:
			self.lastPage()
		elif pageNum<=1:
			self.firstPage()
		else:
			self.origin=(pageNum-1)*self.pageSize



NewPagination=Pagination([1,2,3,4,5,6,7,7,8,9,0,"h",";","y",12,13,14,15,124,16,17,18,19,20,21,22,23,33,24,25,26,27,28,29,30])
NewPagination.getVisibleItems()

NewPagination.nextPage()
NewPagination.getVisibleItems()

NewPagination.nextPage()
NewPagination.getVisibleItems()

NewPagination.prevPage()
NewPagination.getVisibleItems()

NewPagination.firstPage()
NewPagination.getVisibleItems()

NewPagination.lastPage()
NewPagination.getVisibleItems()

NewPagination.goToPage(0)
NewPagination.getVisibleItems()