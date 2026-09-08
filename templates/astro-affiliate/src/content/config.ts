import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    updatedDate: z.date().optional(),
    author: z.string().default('Editorial Team'),
    authorRole: z.string().default('Senior Reviewer'),
    authorAvatar: z.string().optional(),
    image: z.string().optional(),
    category: z.string().default('Review'),
    tags: z.array(z.string()).default([]),
    rating: z.number().min(0).max(10).optional(),
    quickVerdict: z.string().optional(),
    pros: z.array(z.string()).optional(),
    cons: z.array(z.string()).optional(),
    affiliateUrl: z.string().optional(),
    affiliateText: z.string().default('Check Best Price'),
    isFeatured: z.boolean().default(false),
  }),
});

const dealsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    store: z.string(),
    storeSlug: z.string(),
    storeLogo: z.string().optional(),
    code: z.string().optional(),
    discount: z.string(),
    expiryDate: z.string().optional(),
    affiliateUrl: z.string(),
    verified: z.boolean().default(true),
    exclusive: z.boolean().default(false),
    usedCount: z.number().default(128),
    category: z.string().default('General'),
  }),
});

const storesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    slug: z.string().optional(),
    logo: z.string().optional(),
    affiliateUrl: z.string(),
    rating: z.number().min(0).max(5).default(4.8),
    totalCoupons: z.number().default(5),
    bestDiscount: z.string().default('50% Off'),
    description: z.string(),
  }),
});

export const collections = {
  blog: blogCollection,
  deals: dealsCollection,
  stores: storesCollection,
};
