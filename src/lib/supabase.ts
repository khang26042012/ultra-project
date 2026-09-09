import { createClient } from '@supabase/supabase-js';

const supabaseUrl =
  process.env.NEXT_PUBLIC_SUPABASE_URL ||
  'https://dffycwpkbfnaqptuvvju.supabase.co';
const supabaseAnonKey =
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY ||
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRmZnljd3BrYmZuYXFwdHV2dmp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI5NDA4NzgsImV4cCI6MjEwODUxNjg3OH0.hHWZ0haM0sxF_X9mKawdd39bmVp_TdAQKonikyf04Yk';

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
