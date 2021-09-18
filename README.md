
# Objective:
Our core service application allows a user to to many things. A few of these include allowing a user to create a new form template, edit that form template to add fields, submit data against that template, and attach one or more images to the submitted template. 

This repo should contain all you need to satisfy the following request:

    Build a pipline to take all submitted forms, predict their attachment's class using the provided multiclassifier, and output a histogram of class frequency for attachments related only to forms in the "draft" state.

# Access to resources:
## This repo contains 3 folders:
- blob-access (Source for JSON events)
- docker-classifier (Source for the classifier, provided as a standalone docker image)
- funsd-dataset (Source for image files, the image name for attachment events will match a FUNSD image name)

## Potential steps you might take:
1. Pull JSON events from Blob (README in blob-access)
2. Setup the classifier in docker-classifier
3. Load FUNSD Dataset and run a batch predict using the docker-classifier on each form in the FUNSD Dataset. 
4. Enrich the JSON image attachment events with the multi-class scores for that attachments's image (image name for attachment events will match a FUNSD image name)
5. For forms in the 'draft' state with attachments, provide a histogram of the best fitting class for the image

This is a pretty open ended task, more to get a understanding of how hands on you think through a technical problem, how hands on you are, and if you can whip together a rapid prototype / proof of concept for an idea quickly.