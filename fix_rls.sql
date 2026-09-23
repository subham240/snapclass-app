-- ====================================================================
-- SnapClass AI Attendance - Fix Supabase Row Level Security (RLS)
-- Copy and run this script in Supabase: (SQL Editor -> New Query -> Run)
-- ====================================================================

-- 1. Disable Row Level Security on all tables
ALTER TABLE IF EXISTS teachers DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS students DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS subjects DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS subject_students DISABLE ROW LEVEL SECURITY;
ALTER TABLE IF EXISTS attendance_logs DISABLE ROW LEVEL SECURITY;

-- 2. Drop any restrictive policies if they exist
DROP POLICY IF EXISTS "Allow all on teachers" ON teachers;
DROP POLICY IF EXISTS "Allow all on students" ON students;
DROP POLICY IF EXISTS "Allow all on subjects" ON subjects;
DROP POLICY IF EXISTS "Allow all on subject_students" ON subject_students;
DROP POLICY IF EXISTS "Allow all on attendance_logs" ON attendance_logs;

-- 3. In case Supabase forces RLS to remain enabled, create universal permissive policies:
ALTER TABLE IF EXISTS teachers ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow all on teachers" ON teachers FOR ALL USING (true) WITH CHECK (true);

ALTER TABLE IF EXISTS students ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow all on students" ON students FOR ALL USING (true) WITH CHECK (true);

ALTER TABLE IF EXISTS subjects ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow all on subjects" ON subjects FOR ALL USING (true) WITH CHECK (true);

ALTER TABLE IF EXISTS subject_students ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow all on subject_students" ON subject_students FOR ALL USING (true) WITH CHECK (true);

ALTER TABLE IF EXISTS attendance_logs ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow all on attendance_logs" ON attendance_logs FOR ALL USING (true) WITH CHECK (true);
