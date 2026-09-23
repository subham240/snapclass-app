-- ====================================================================
-- SnapClass AI Attendance System - Supabase PostgreSQL Database Schema
-- Run this script in your Supabase SQL Editor (SQL Editor -> New Query -> Run)
-- ====================================================================

-- 1. Create Teachers table
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id BIGSERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 2. Create Students table
CREATE TABLE IF NOT EXISTS students (
    student_id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    face_embedding JSONB DEFAULT NULL,
    voice_embedding JSONB DEFAULT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Create Subjects table
CREATE TABLE IF NOT EXISTS subjects (
    subject_id BIGSERIAL PRIMARY KEY,
    subject_code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    section TEXT NOT NULL,
    teacher_id BIGINT REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 4. Create Subject Enrollment (subject_students) table
CREATE TABLE IF NOT EXISTS subject_students (
    id BIGSERIAL PRIMARY KEY,
    student_id BIGINT REFERENCES students(student_id) ON DELETE CASCADE,
    subject_id BIGINT REFERENCES subjects(subject_id) ON DELETE CASCADE,
    enrolled_at TIMESTAMPTZ DEFAULT now(),
    CONSTRAINT unique_student_subject UNIQUE (student_id, subject_id)
);

-- 5. Create Attendance Logs table
CREATE TABLE IF NOT EXISTS attendance_logs (
    id BIGSERIAL PRIMARY KEY,
    student_id BIGINT REFERENCES students(student_id) ON DELETE CASCADE,
    subject_id BIGINT REFERENCES subjects(subject_id) ON DELETE CASCADE,
    timestamp TEXT NOT NULL,
    is_present BOOLEAN DEFAULT false
);

-- 6. Disable Row Level Security (RLS) for seamless client-side access using Supabase Anon/Service Key
ALTER TABLE teachers DISABLE ROW LEVEL SECURITY;
ALTER TABLE students DISABLE ROW LEVEL SECURITY;
ALTER TABLE subjects DISABLE ROW LEVEL SECURITY;
ALTER TABLE subject_students DISABLE ROW LEVEL SECURITY;
ALTER TABLE attendance_logs DISABLE ROW LEVEL SECURITY;

-- Or alternative: If you prefer RLS enabled, uncomment below to grant full anon access:
-- ALTER TABLE teachers ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "Allow full access to teachers" ON teachers FOR ALL USING (true) WITH CHECK (true);
-- ALTER TABLE students ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "Allow full access to students" ON students FOR ALL USING (true) WITH CHECK (true);
-- ALTER TABLE subjects ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "Allow full access to subjects" ON subjects FOR ALL USING (true) WITH CHECK (true);
-- ALTER TABLE subject_students ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "Allow full access to subject_students" ON subject_students FOR ALL USING (true) WITH CHECK (true);
-- ALTER TABLE attendance_logs ENABLE ROW LEVEL SECURITY;
-- CREATE POLICY "Allow full access to attendance_logs" ON attendance_logs FOR ALL USING (true) WITH CHECK (true);
