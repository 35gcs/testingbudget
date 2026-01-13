# Railway Deployment Checklist

Use this checklist to deploy your Youth Sports Budget app to Railway.

## Pre-Deployment

- [ ] All code changes committed to Git
- [ ] Code pushed to GitHub repository
- [ ] Railway account created
- [ ] Generated SECRET_KEY (run: `python -c "import secrets; print(secrets.token_urlsafe(32))"`)

---

## Railway Setup

### 1. Create Project
- [ ] Go to [railway.app](https://railway.app)
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub repo"
- [ ] Choose your repository

### 2. Add Database
- [ ] Click "New" in project
- [ ] Select "Database" → "PostgreSQL"
- [ ] Wait for database to provision
- [ ] Verify `DATABASE_URL` is added to your service variables

### 3. Configure Service
- [ ] Click on your service
- [ ] Go to **Settings** tab
- [ ] Under **Source**, set **Root Directory** to: `backend`
- [ ] Save changes

### 4. Set Environment Variables
- [ ] Go to **Variables** tab
- [ ] Add variable: `SECRET_KEY` = (paste your generated key)
- [ ] Verify `DATABASE_URL` exists (auto-added by PostgreSQL)
- [ ] Verify `PORT` is set to `${{PORT}}` (or not set - Railway handles it)

### 5. Deploy
- [ ] Click **Deploy** button (or it auto-deploys)
- [ ] Wait for build to complete
- [ ] Check deployment logs for errors

---

## Verify Deployment

### Check Endpoints
- [ ] Visit: `https://your-app.railway.app/`
  - Should show: `{"message": "Youth Sports Budget API", ...}`
- [ ] Visit: `https://your-app.railway.app/health`
  - Should show: `{"status": "healthy"}`
- [ ] Visit: `https://your-app.railway.app/docs`
  - Should show API documentation

### Check Logs
- [ ] Go to Railway Dashboard → Your Service → Deployments
- [ ] Click latest deployment
- [ ] View logs for "✅ Database initialized"
- [ ] No errors in startup logs

---

## Frontend Deployment (Netlify)

### 1. Create Site
- [ ] Go to [netlify.com](https://netlify.com)
- [ ] Click "Add new site"
- [ ] Connect GitHub repository
- [ ] Build settings auto-detected from `netlify.toml`

### 2. Set Environment Variable
- [ ] Go to Site settings → Environment variables
- [ ] Add variable:
  - Key: `VITE_API_URL`
  - Value: `https://your-railway-app.railway.app/api/v1`

### 3. Deploy
- [ ] Click "Deploy site"
- [ ] Wait for build to complete
- [ ] Visit your Netlify URL

---

## Update CORS

After frontend is live:

### Option A: Environment Variable (Recommended)
- [ ] Railway → Your Service → Variables
- [ ] Add: `CORS_ORIGINS` = `https://your-app.netlify.app`
- [ ] Redeploy if needed

### Option B: Code Change
- [ ] Edit `backend/app/main.py` line 38
- [ ] Change `["*"]` to `allowed_origins`
- [ ] Commit and push (auto-deploys to Railway)

---

## Final Testing

- [ ] Frontend loads successfully
- [ ] Can create an organization
- [ ] Can create a season
- [ ] Can add a team
- [ ] Can log expenses
- [ ] Can add revenue
- [ ] Dashboard shows correct data
- [ ] No CORS errors in browser console
- [ ] API calls going to correct backend URL

---

## Post-Deployment

- [ ] Save Railway backend URL
- [ ] Save Netlify frontend URL
- [ ] Test all major features
- [ ] Monitor Railway logs for errors
- [ ] Consider setting up custom domain
- [ ] Review authentication settings for production

---

## Common Issues

### ❌ "Module not found" error
**Fix**: Set Root Directory to `backend` in Railway settings

### ❌ "Database connection failed"
**Fix**: Ensure PostgreSQL is added and `DATABASE_URL` is set

### ❌ "SECRET_KEY not set" warning
**Fix**: Add SECRET_KEY environment variable in Railway

### ❌ CORS errors in browser
**Fix**: Set `CORS_ORIGINS` to your Netlify URL

### ❌ Frontend shows "Network Error"
**Fix**: Check `VITE_API_URL` in Netlify settings

---

## Support

- See `RAILWAY_DEPLOYMENT_GUIDE.md` for detailed instructions
- See `BUGFIXES_SUMMARY.md` for what was fixed
- See `FINAL_SETUP_GUIDE.md` for complete setup process

---

**Ready to deploy? Start with the Pre-Deployment checklist above!** ✅
