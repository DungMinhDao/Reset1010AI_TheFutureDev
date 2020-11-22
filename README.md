# Integrated Expertise Training Platform - AI solution

## Our team: TheFutureDev
| Name |Email | Slack Account |
| ------ | --------------- | ---------------- |
| Nguyen Duc Chinh| chinhbka@gmail.com | [Nguyen Duc Chinh - TheFutureDev] |
| Dao Minh Dung | dungdao3112000@gmail.com | [Dao Minh Dung - TheFutureDev] |
| Nguyen Trong Hai | tronghaixh2000@gmail.com | [Nguyen Trong Hai - TheFutureDev] |
| Phan Viet Hoang| phanviethoang1512@gmail.com | [Phan Viet Hoang - TheFutureDev] |
| Nguyen Van Trinh| vantrinh2607@gmail.com | [Nguyen Van Trinh - TheFutureDev] |

## Problem
  Employees are facing issues in searching for suitable courses and building individualized learning paths, as well as creating a system where employees can track their skills and career goals.
  
## Solution
 - Our solution is an integrated platform, with automatic courses suggestion and learning paths construction from a wide variety of available and trusted sources, as well as a way to track the employees’ career development path and skills needed to achieve career goals.
 -The system automatically suggests learning pathways based on existing skills, specialized skills needed to develop, and personal targets.
  
## AI features
Here is our demo for the AI system that we have built in the last two days
  
### Main structure
![Untitled Document (4)](https://user-images.githubusercontent.com/52401767/99893169-6a584200-2caf-11eb-90d8-0c6e1d5fb60f.png)


### Main flow
#### Training
- First the training documents are processed (cleaning, tokenizing) then passed to an embedding model to get their representation vectors
- The acquired vectors are passed to a cluster model (Kmeans in this case), this will group our documents into sub classes which sharea common semantic and syntactic features
- The trained model (including tokenizer, clustering model, clustered training document) will be save into database for easy usage as well as inference speed
#### Inferencing
- User queries are processed exactly the same as in the case of training document to get their embeddings
- With a trained model from database, users will get the recommended course base on the context of their queries

### Future direction
#### Model improvement
- We plan to use state-of-the-art model in NLP for text encoder (transformer-based model)
#### Get more user information
- We are in lack of users' data and will collect more information from users to improve our model

