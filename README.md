http://travel-agency-project-s3.s3-website-us-east-1.amazonaws.com/

# Travel Agency

***This is my experimental full-stack website designed to strengthen deployment and cloud infrastructure skills.***

**Frontend:** React (Vite)  
**Backend:** Flask  
**Database:** PostgreSQL (RDS) !

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
  
<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/a40469d8-521b-41ca-b92b-f83be4e7bc3e" />

<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/edd699a1-352c-4a63-b8ad-b5450dd581b2" />

cd backend
docker build -t travel-backend .
docker run -d -p 8080:8080 travel-backend
