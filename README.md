# Travel Agency

***This is my experimental full-stack website designed to strengthen deployment and cloud infrastructure skills.***

**Frontend:** React (Vite)  
**Backend:** Flask  
**Database:** PostgreSQL (RDS) !
**Deployment:** AWS


## Current Deployment
The website is currently deployed using:  
- **S3 bucket** for static assets  
- **EC2 instance** for the backend  
- **RDS** for PostgreSQL database !

## Next Steps
Planned enhancements include integrating:  
- **Auto Scaling Group (ASG)**  
- **Application Load Balancer (ALB)**  
- **CloudFront** for the S3 bucket
- **SSL/TLS Certificate** for secure connections  
- **Custom Domain** configuration using Route 53
  
<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/e82e8cda-475b-4e85-a9a3-643637534ec6" />

<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/285423cb-28f5-4e33-b204-fbdb55e2d616" />

cd backend
docker build -t travel-backend .
docker run -d -p 8080:8080 travel-backend
