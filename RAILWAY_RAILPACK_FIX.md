# Railway Railpack Error - Complete Fix

## The Error
```
railpack process exited with an error
```

This means Railway's Nixpacks builder cannot build your app. Here's the exact fix:

---

## Step 1: Check Railway Service Settings

**CRITICAL: These settings MUST be exactly right**

### Go to Railway Dashboard:
1. Click on your service (not the database)
2. Go to **Settings** tab
3. Check these settings:

#### Root Directory
**Must be exactly**: `backend`
- If it says `backend/` (with slash) → Remove the slash
- If it's empty → Set it to `backend`
- If it says anything else → Change it to `backend`

#### Start Command (Optional)
Railway should auto-detect from Procfile, but if you need to set it manually:
```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**DO NOT USE** `python -m uvicorn` - just use `uvicorn`

#### Build Command
**Leave this EMPTY** - Railway auto-detects from requirements.txt

---

## Step 2: Check Environment Variables

Go to **Variables** tab and verify:

### Required Variables
- [ ] `DATABASE_URL` - Should be auto-set by PostgreSQL plugin
- [ ] `SECRET_KEY` - You must add this manually

### Generate SECRET_KEY
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the output and add it as `SECRET_KEY` in Railway variables.

### Optional Variables
- `PORT` - Railway auto-sets this, don't add it manually
- `CORS_ORIGINS` - Add your frontend URL later

---

## Step 3: Verify PostgreSQL Database

1. In your Railway project, you should see **two services**:
   - Your app service
   - PostgreSQL database

2. If you don't see PostgreSQL:
   - Click **New** → **Database** → **PostgreSQL**
   - Railway will automatically link it and set `DATABASE_URL`

---

## Step 4: Force Redeploy

After fixing settings:

1. Go to **Deployments** tab
2. Click the three dots (...) on the latest deployment
3. Click **Redeploy**

Or trigger a new deployment:
- Make any small change in your code
- Push to GitHub
- Railway will auto-deploy

---

## Step 5: Check Deployment Logs

**This is the most important step for debugging:**

1. Go to **Deployments** tab
2. Click on the latest deployment
3. Click **View Logs**
4. **Scroll all the way to the bottom** - the actual error is at the end

### Common Errors You Might See:

#### Error: "No module named 'app'"
**Cause**: Root Directory not set to `backend`
**Fix**: Settings → Root Directory = `backend`

#### Error: "ModuleNotFoundError: No module named 'fastapi'"
**Cause**: Dependencies not installing
**Fix**: Check requirements.txt exists in backend/ folder

#### Error: "uvicorn: command not found"
**Cause**: Start command issue
**Fix**: Make sure start command is just `uvicorn` not `python -m uvicorn`

#### Error: "Database connection failed"
**Cause**: PostgreSQL not added or DATABASE_URL not set
**Fix**: Add PostgreSQL database to project

#### Error: "SECRET_KEY not set"
**This is just a warning** - app will work but you should set SECRET_KEY

---

## Alternative: Delete and Recreate Service

If settings won't take effect:

1. **Delete the service** (NOT the database):
   - Go to service Settings
   - Scroll down to "Danger Zone"
   - Click "Delete Service"

2. **Create new service**:
   - Click **New** → **GitHub Repo**
   - Select `35gcs/testingbudget`
   - Railway will create a new service

3. **Set Root Directory immediately**:
   - Before it finishes deploying
   - Settings → Root Directory = `backend`

4. **Add SECRET_KEY**:
   - Variables tab
   - Add `SECRET_KEY` with your generated value

5. **Wait for deployment**

---

## Verify It's Working

Once deployed successfully, test these URLs:

1. **Health Check**: `https://your-app.railway.app/health`
   - Should return: `{"status": "healthy"}`

2. **API Docs**: `https://your-app.railway.app/docs`
   - Should show interactive API documentation

3. **Root**: `https://your-app.railway.app/`
   - Should return: `{"message": "Youth Sports Budget API", ...}`

---

## Configuration Files (Already Fixed)

✅ `backend/railway.json` - Simplified
✅ `backend/Procfile` - Uses `uvicorn` directly
✅ `backend/nixpacks.toml` - Updated to Python 3.11
✅ `backend/.python-version` - Set to 3.11
✅ `backend/requirements.txt` - All dependencies listed

These files are now correct in your GitHub repo.

---

## Quick Checklist

Use this to verify everything:

- [ ] Railway project created
- [ ] PostgreSQL database added to project
- [ ] Service Root Directory = `backend` (no trailing slash)
- [ ] `SECRET_KEY` environment variable set
- [ ] `DATABASE_URL` exists (auto-set by PostgreSQL)
- [ ] Latest code from GitHub (`3821031` commit or later)
- [ ] Deployment attempted
- [ ] Checked deployment logs for specific error

---

## Still Getting Error?

If you still see "railpack process exited with an error":

1. **Share the actual error from logs**:
   - Go to Deployments → Latest deployment → View Logs
   - Scroll to the **very bottom**
   - Copy the last 20-30 lines
   - Share those lines with me

2. **Verify your settings**:
   - Take a screenshot of Settings → Root Directory
   - Take a screenshot of Variables tab
   - Share those with me

The actual error message in the logs will tell us exactly what's wrong.

---

## Expected Successful Build Logs

When it works, you should see:

```
==> Building with Nixpacks
==> Installing Python 3.11
==> Installing requirements from requirements.txt
Successfully installed fastapi-... uvicorn-... sqlalchemy-...
==> Starting application
✅ Database initialized
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:XXXX
```

---

**The configuration is now correct in your GitHub repo. The issue is likely in your Railway service settings, specifically the Root Directory.**
