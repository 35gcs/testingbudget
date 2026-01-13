# Railway Deployment Guide

This guide will help you deploy the Youth Sports Budget application to Railway.

## Prerequisites

- A [Railway](https://railway.app) account
- Your code pushed to a GitHub repository
- Basic understanding of environment variables

## Step 1: Create Railway Project

1. Go to [Railway](https://railway.app) and sign in
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository
5. Railway will create a new project

## Step 2: Add PostgreSQL Database

1. In your Railway project, click **"New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Railway will automatically create a PostgreSQL database
4. The `DATABASE_URL` environment variable will be automatically added to your service

## Step 3: Configure Backend Service

### Set Root Directory

1. Click on your backend service
2. Go to **Settings**
3. Under **Source**, set **Root Directory** to: `backend`
4. Click **Save**

### Set Environment Variables

1. Go to the **Variables** tab
2. Add the following variables:

```
SECRET_KEY=<generate-secure-key>
PORT=${{PORT}}
```

**To generate a secure SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

**Note:** `DATABASE_URL` is automatically set by Railway when you add PostgreSQL.

### Set Start Command (Optional)

Railway should auto-detect the start command from `Procfile`, but if needed:

1. Go to **Settings**
2. Under **Deploy**, set **Start Command** to:
```
python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Step 4: Deploy

1. Click **Deploy** or push changes to your GitHub repository
2. Railway will automatically deploy your application
3. Wait for the deployment to complete (check the logs)
4. Once deployed, Railway will provide you with a public URL

## Step 5: Verify Deployment

Visit your Railway URL with these endpoints:

- **Health Check**: `https://your-app.railway.app/health`
- **API Docs**: `https://your-app.railway.app/docs`
- **Root**: `https://your-app.railway.app/`

## Environment Variables Summary

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `DATABASE_URL` | Yes | Auto-set by Railway PostgreSQL | Auto-generated |
| `SECRET_KEY` | Yes | JWT secret key | Generate with secrets.token_urlsafe(32) |
| `PORT` | Yes | Port (use Railway's $PORT) | `${{PORT}}` |
| `CORS_ORIGINS` | Optional | Allowed frontend URLs | `https://your-frontend.netlify.app` |
| `REQUIRE_AUTH` | Optional | Enforce authentication | `false` (development) |

## Troubleshooting

### Issue: "Module not found"
**Solution:** Make sure Root Directory is set to `backend` in Railway settings.

### Issue: "Database connection failed"
**Solution:**
1. Check that PostgreSQL database is added to your project
2. Verify `DATABASE_URL` is set in environment variables
3. Check deployment logs for specific error

### Issue: "Port binding failed"
**Solution:** Ensure start command uses `--port $PORT` (not hardcoded port).

### Issue: "Application won't start"
**Solution:**
1. Check deployment logs in Railway dashboard
2. Ensure all dependencies in `requirements.txt` are correct
3. Verify Python version compatibility

### Issue: "SECRET_KEY warning"
**Solution:** Set the `SECRET_KEY` environment variable in Railway.

## Updating CORS for Frontend

Once you deploy your frontend (e.g., to Netlify), update the CORS settings:

1. Go to Railway → Your Service → Variables
2. Add or update `CORS_ORIGINS`:
```
CORS_ORIGINS=https://your-frontend.netlify.app,http://localhost:3000
```

Or update `app/main.py` line 22 to use specific origins instead of `["*"]`.

## Monitoring

- **Logs**: Railway Dashboard → Your Service → Deployments → Click deployment → View Logs
- **Metrics**: Railway Dashboard → Your Service → Metrics
- **Database**: Railway Dashboard → PostgreSQL → Data tab

## Production Checklist

- [ ] PostgreSQL database added and connected
- [ ] `SECRET_KEY` environment variable set (secure random key)
- [ ] `DATABASE_URL` environment variable set by Railway
- [ ] Root Directory set to `backend`
- [ ] CORS origins configured for your frontend domain
- [ ] Health check endpoint (`/health`) returns 200 OK
- [ ] API documentation accessible at `/docs`
- [ ] Consider enabling authentication (`REQUIRE_AUTH=true`)

## Next Steps

1. Deploy frontend to Netlify or Vercel
2. Update frontend's `VITE_API_URL` to point to Railway backend URL
3. Update CORS settings in backend to allow frontend domain
4. Test the full application flow
5. Consider setting up custom domain

## Support

- [Railway Documentation](https://docs.railway.app/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Project Issues](https://github.com/your-repo/issues)
