# HackathonInfoxOuO

This project's drive is to minimize the size of a PDF file by eliminating image duplicates. 
The idea is to create a reference of the images and each time a duplicate is presented on the file, substituting 
that image with a reference, thus minimizing the total size of the PDF.

## Approach
The approach taken by our group was to research the composition of PDFs and how they work. As to get a little 
more insight to the problem that lied ahead. Once we had an idea of how PDFs files were structured internally
we drew a plan to attack the problem. First we were to determine the specific layout of the file, then we were
to extract the images and create the references, finaly we were to replace the duplicates with the references.

## Conclusion
We were able to find and extract the references of the images we wanted (thos on the first page od the file), but
hit a bottle neck on the replacement of the duplicates with the references. We were able to Iterate through the file
and attach the references throughout, but were having problems deleting the data of the duplicates. All in all
our approach granted us a whooping 0.8 MB size reduction!! Small wins...
